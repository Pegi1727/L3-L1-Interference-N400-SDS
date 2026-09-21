% 02_permutation_tests_and_fdr.m
% Nonparametric permutation tests (10,000 iterations) + Benjamini-Hochberg FDR (Table 4)
% Base MATLAB only. Run from scripts/ directory.
T = readtable('../data/study_dataset_full_3condition.csv');
nPerm = 10000; rng(42);
contrasts = { % {name, time, groupA, groupB, conditionA, conditionB}
 'Congruent_vs_StronglyIncongruent_Exp_Posttest','Posttest','Experimental','Experimental','Congruent','Strongly_Incongruent'};
p_raw = []; names = {}; obs_all = [];
for c = 1:size(contrasts,1)
    sel = strcmp(T.Time, contrasts{c,2}) & strcmp(T.Group, contrasts{c,3}) & ...
          (strcmp(T.Condition, contrasts{c,5}) | strcmp(T.Condition, contrasts{c,6}));
    x = T.N400_amplitude(sel & strcmp(T.Condition, contrasts{c,5}));
    y = T.N400_amplitude(sel & strcmp(T.Condition, contrasts{c,6}));
    obs = mean(x) - mean(y); allv = [x(:); y(:)]; nx = numel(x); n = numel(allv);
    ge = 0;
    for p = 1:nPerm
        ix = randperm(n);
        d = mean(allv(ix(1:nx))) - mean(allv(ix(nx+1:end)));
        ge = ge + (abs(d) >= abs(obs));
    end
    p_raw(end+1) = (ge+1)/(nPerm+1); %#ok<*SAGROW>
    names{end+1} = contrasts{c,1}; obs_all(end+1) = obs;
    fprintf('%s: diff = %.4f, p = %.5f\n', names{end}, obs, p_raw(end));
end
% Benjamini-Hochberg FDR correction
[m, order] = sort(p_raw); adj = zeros(1,m);
adj(order) = min(1, cummin((1:m)' .* m ./ (1:m)')); % BH step-up
% If Statistics Toolbox available: adj = fdr_bh(p_raw);
fprintf('\nFDR-corrected p-values:\n');
for i = 1:numel(names), fprintf('%s: p_adj = %.5f\n', names{i}, adj(i)); end
