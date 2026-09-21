% 01_preprocess_and_extract_n400.m
% EEG preprocessing: bandpass 0.1-30 Hz, ICA artifact removal (ICLabel), N400 extraction
% Requires EEGLAB 2023+ and ICLabel
addpath(eeglab); eeglab nogui;
load('sample_eeg/sub-01_task-rsvp_raw.mat');
EEG = eeg_emptyset; EEG.data = data; EEG.srate = srate; EEG.nbchan = nbchan;
EEG.pnts = pnts; EEG.trials = trials;
for k = 1:numel(chanlocs_labels), EEG.chanlocs(k).labels = chanlocs_labels{k}; end
EEG = eeg_checkset(EEG);
EEG = pop_eegfiltnew(EEG, 0.1, 30);          % bandpass 0.1-30 Hz
EEG = pop_reref(EEG, []);                    % average reference
EEG = pop_runamica(EEG, 'chan_dim', 1);      % ICA decomposition
EEG = pop_iclabel(EEG, 'default');           % automatic artifact classification
labels = [EEG.etc.icclassification.class_labels];
probs  = cell2mat({EEG.etc.icclassification.class_prob});
bad = find(max(probs, [], 2) > 0.5 & ismember(labels, 1:3));  % eye/muscle components
EEG = pop_subcomp(EEG, bad, 0);
EEG = pop_epoch(EEG, {'101','102','103'}, [-0.2 0.8], 'newname', 'N400 epochs');
EEG = pop_baseline(EEG, [], 0);
win = round([0.35 0.5]*EEG.srate) + 1;
roi = {'Cz','C1','C2','C3','C4','CP1','CP2','CPz','Pz','P1','P2','FCz','FC1','FC2'};
idx = ismember({EEG.chanlocs.labels}, roi);
N400 = squeeze(mean(mean(EEG.data(idx, win(1):win(2), :), 2), 1));
fprintf('N400 mean amplitude extracted: %d epochs\n', numel(N400));
save('N400_epochs_preprocessed.mat','EEG');
