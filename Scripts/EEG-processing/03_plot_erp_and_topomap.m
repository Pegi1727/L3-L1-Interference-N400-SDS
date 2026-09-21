% 03_plot_erp_and_topomap.m
% Grand-average ERP waveforms with +/-1 SEM ribbons and scalp topographies (requires EEGLAB)
addpath(eeglab); eeglab nogui;
load('N400_epochs_preprocessed.mat');   % output of script 01
times = EEG.times/1000;
conds = {'101','102','103'}; names = {'Congruent','Moderately_Incongruent','Strongly_Incongruent'};
roi = {'Cz','C1','C2','C3','C4','CP1','CP2','CPz','Pz','P1','P2','FCz','FC1','FC2'};
idx = ismember({EEG.chanlocs.labels}, roi);
figure; hold on;
cols = lines(3);
for c = 1:3
    erp = mean(mean(EEG.data(idx, :, strcmp({EEG.etc.condition}, conds{c})), 1), 3);
    sem = std(mean(EEG.data(idx, :, strcmp({EEG.etc.condition}, conds{c})), 1), 0, 3)/sqrt(EEG.trials);
    plot(times, erp, 'Color', cols(c,:), 'LineWidth', 1.5);
    patch([times fliplr(times)], [erp+sem fliplr(erp-sem)], cols(c,:), 'FaceAlpha', 0.15, 'EdgeColor','none');
end
legend(names); xlabel('Time (s)'); ylabel('Amplitude (\muV)');
title('Grand-average ERP at centro-parietal ROI (±1 SEM)');
figure; pop_topoplot(EEG, 0, 0, '', 'N400 (350-500 ms)', [0.35 0.5], 'plotopt', {'style','map','electrodes','labels'});
