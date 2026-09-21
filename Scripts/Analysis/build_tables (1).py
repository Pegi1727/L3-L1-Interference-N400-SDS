import pandas as pd
import os

t1_data = [
    ["N400 Amplitude (μV)", "CG", "T1", "2.81 ± 1.00", "3.59 ± 1.05", "7.57 ± 1.96"],
    ["N400 Amplitude (μV)", "CG", "T2", "3.14 ± 1.15", "3.53 ± 1.13", "7.87 ± 2.18"],
    ["N400 Amplitude (μV)", "CG", "T3", "3.08 ± 1.08", "3.68 ± 1.05", "7.93 ± 2.66"],
    ["N400 Amplitude (μV)", "EG", "T1", "3.38 ± 1.25", "3.69 ± 1.26", "8.57 ± 1.90"],
    ["N400 Amplitude (μV)", "EG", "T2", "2.77 ± 1.10", "3.31 ± 1.13", "6.58 ± 2.27"],
    ["N400 Amplitude (μV)", "EG", "T3", "2.36 ± 0.99", "2.63 ± 0.97", "5.62 ± 2.33"],
    ["Reaction Time (ms)", "CG", "T1", "668.0 ± 101.4", "905.7 ± 124.9", "1720.8 ± 192.5"],
    ["Reaction Time (ms)", "CG", "T2", "643.9 ± 95.8", "880.8 ± 109.9", "1624.8 ± 207.6"],
    ["Reaction Time (ms)", "CG", "T3", "668.6 ± 106.6", "895.8 ± 116.8", "1695.2 ± 213.2"],
    ["Reaction Time (ms)", "EG", "T1", "687.2 ± 117.8", "906.9 ± 128.8", "1735.6 ± 227.7"],
    ["Reaction Time (ms)", "EG", "T2", "683.9 ± 115.1", "897.4 ± 104.9", "1678.1 ± 232.4"],
    ["Reaction Time (ms)", "EG", "T3", "598.1 ± 88.0", "760.3 ± 113.6", "1493.1 ± 183.1"],
    ["Oral Fluency (Score)", "CG", "T1", "11.00 ± 2.01", "10.15 ± 2.05", "4.48 ± 1.22"],
    ["Oral Fluency (Score)", "CG", "T2", "11.08 ± 1.98", "10.05 ± 1.88", "4.40 ± 1.22"],
    ["Oral Fluency (Score)", "CG", "T3", "11.20 ± 2.08", "10.22 ± 1.83", "4.45 ± 1.15"],
    ["Oral Fluency (Score)", "EG", "T1", "10.68 ± 2.04", "9.92 ± 2.21", "4.08 ± 1.07"],
    ["Oral Fluency (Score)", "EG", "T2", "11.60 ± 1.96", "10.65 ± 1.83", "4.68 ± 1.31"],
    ["Oral Fluency (Score)", "EG", "T3", "12.18 ± 1.96", "11.20 ± 1.84", "5.30 ± 1.45"],
    ["L1 Pragmatic Reliance", "CG", "T1", "2.38 ± 1.05", "3.58 ± 1.24", "8.05 ± 1.77"],
    ["L1 Pragmatic Reliance", "CG", "T2", "2.22 ± 0.97", "3.45 ± 1.15", "8.02 ± 1.62"],
    ["L1 Pragmatic Reliance", "CG", "T3", "2.12 ± 0.88", "3.35 ± 1.10", "8.05 ± 1.58"],
    ["L1 Pragmatic Reliance", "EG", "T1", "2.60 ± 0.96", "3.80 ± 1.30", "8.65 ± 1.66"],
    ["L1 Pragmatic Reliance", "EG", "T2", "2.15 ± 1.03", "3.15 ± 1.27", "7.78 ± 1.87"],
    ["L1 Pragmatic Reliance", "EG", "T3", "1.72 ± 0.82", "2.62 ± 1.03", "6.48 ± 1.91"],
    ["L1 Calque Errors", "CG", "T1", "2.03 ± 1.19", "3.97 ± 1.89", "10.66 ± 3.61"],
    ["L1 Calque Errors", "CG", "T2", "2.12 ± 1.34", "3.90 ± 1.84", "10.14 ± 3.55"],
    ["L1 Calque Errors", "CG", "T3", "2.15 ± 1.37", "3.89 ± 1.80", "10.15 ± 3.55"],
    ["L1 Calque Errors", "EG", "T1", "2.07 ± 1.19", "4.00 ± 1.85", "9.99 ± 3.93"],
    ["L1 Calque Errors", "EG", "T2", "1.52 ± 1.18", "2.95 ± 1.58", "7.48 ± 3.25"],
    ["L1 Calque Errors", "EG", "T3", "1.02 ± 0.97", "1.98 ± 1.37", "5.28 ± 3.22"],
]
df_t1 = pd.DataFrame(t1_data, columns=["Measure", "Group", "Time", "Control (M±SD)", "Target (M±SD)", "Mismatch (M±SD)"])

t2_data = [
    ["N400 Amplitude", "Group", 39.52, "1, 78", 39.52, 5.631, ".020", 0.067],
    ["N400 Amplitude", "Time", 16.92, "2, 156", 8.46, 5.542, ".005", 0.066],
    ["N400 Amplitude", "Condition", 2697.57, "2, 156", 1348.78, 1120.007, "< .001", 0.935],
    ["N400 Amplitude", "Group × Time", 34.19, "2, 156", 17.10, 11.199, "< .001", 0.126],
    ["N400 Amplitude", "Group × Condition", 17.88, "2, 156", 8.94, 7.426, "< .001", 0.087],
    ["N400 Amplitude", "Time × Condition", 8.89, "4, 312", 2.22, 4.390, ".002", 0.053],
    ["N400 Amplitude", "Group × Time × Condition", 11.20, "4, 312", 2.80, 5.527, "< .001", 0.066],
    ["Reaction Time", "Group", 143329.8, "1, 78", 143329.8, 1.496, ".225", 0.019],
    ["Reaction Time", "Time", 174668.7, "2, 156", 87334.3, 7.577, "< .001", 0.089],
    ["Reaction Time", "Condition", 118432364.5, "2, 156", 59216182.3, 7265.695, "< .001", 0.989],
    ["Reaction Time", "Group × Time", 228148.9, "2, 156", 114074.4, 9.897, "< .001", 0.113],
    ["Reaction Time", "Group × Condition", 49441.7, "2, 156", 24720.8, 3.033, ".051", 0.037],
    ["Reaction Time", "Time × Condition", 84501.9, "4, 312", 21125.5, 6.258, "< .001", 0.074],
    ["Reaction Time", "Group × Time × Condition", 59430.7, "4, 312", 14857.7, 4.401, ".002", 0.053],
    ["Oral Fluency", "Group", 29.58, "1, 78", 29.58, 5.524, ".021", 0.066],
    ["Oral Fluency", "Time732, ".010", 0. 156", 4.58, 4.732, ".010", 0.057],
    ["Oral Fluency", "Condition", 7078.69, "2, 156", 3539.35, 7280.970, "< .001", 0.989],
    ["Oral Fluency", "Group × Time", 6.00, "2, 156", 3.00, 3.093, ".048", 0.038],
    ["Oral Fluency", "Group × Condition", 0.39, "2, 156", 0.20, 0.404, ".669", 0.005],
    ["Oral Fluency", "Time × Condition", 2.50, "4, 312", 0.63, 1.814, ".126", 0.023],
    ["Oral Fluency", "Group × Time × Condition", 1.85, "4, 312", 0.46, 1.336, ".256", 0.017],
    ["L1 Pragmatic Reliance", "Group", 17.51, "1, 78", 17.51, 4.597, ".035", 0.056],
    ["L1 Pragmatic Reliance", "Time", 25.13, "2, 156", 12.56, 18.602, "< .001", 0.193],
    ["L1 Pragmatic Reliance", "Condition", 3704.99, "2, 156", 1852.49, 1647.830, "< .001", 0.955],
    ["L1 Pragmatic Reliance", "Group × Time", 4.55, "2, 156", 2.28, 3.371, ".037", 0.041],
    ["L1 Pragmatic Reliance", "Group × Condition", 8.48, "2, 156", 4.24, 3.770, ".025", 0.046],
    ["L1 Pragmatic Reliance", "Time × Condition", 9.38, "4, 312", 2.35, 5.418, "< .001", 0.065],
    ["L1 Pragmatic Reliance", "Group × Time × Condition", 2.50, "4, 312", 0.63, 1.444, ".219", 0.018],
    ["L1 Calque Errors", "Group", 373.19, "1, 78", 373.19, 41.043, "< .001", 0.345],
    ["L1 Calque Errors", "Time", 94.75, "2, 156", 47.37, 11.071, "< .001", 0.124],
    ["L1 Calque Errors", "Condition", 6791.66, "2, 156", 3395.83, 985.394, "< .001", 0.927],
    ["L1 Calque Errors", "Group × Time", 55.63, "2, 156", 27.82, 6.501, ".002", 0.077],
    ["L1 Calque Errors", "Group × Condition", ,.47, "2, 156", 101.23, 29.375, "< .001", 0.274],
    ["L1 Calque Errors", "Time × Condition", 46.12, "4, 312", 11.53, 6.386, "< .001", 0.076],
    ["L1 Calque Errors", "Group × Time × Condition", 37.28, "4, 312", 9.32, 5.161, "< .001", 0.062],
]
df_t2 = pd.DataFrame(t2_data, columns=["Measure", "Source", "SS", "df", "MS", "F", "p", "η_p^2"])

t3_data = [
    ["N400 Violation Cost (μV)", "Baseline (T1)", "5.19 ± 1.76", "4.76 ± 1.77", "t(78) = 1.09", ".278", "0.24", "Non-significant"],
    ["N400 Violation Cost (μV)", "Retention (T3)", "3.26 ± 1.84", "4.85 ± 2.24", "t(78) = -3.46", "< .001", "0.77", "Significant (EG lower cost)"],
    ["RT Violation Cost (ms)", "Baseline (T1)", "1048.4 ± 176.6", "1052.8 ± 153.2", "t(78) = -0.12", ".906", "0.03", "Non-significant"],
    ["RT Violation Cost (ms)", "Retention (T3)", "895.0 ± 145.2", "1026.6 ± 168.4", "t(78) = -3.74", "< .001", "0.84", "Significant (EG lower cost)"],
    ["Calque Error Cost", "Baseline (T1)", "7.92 ± 3.23", "8.63 ± 2.87", "t(78) = -1.04", ".301", "0.23", "Non-significant"],
    ["Calque Error Cost", "Retention (T3)", "4.26 ± 2.65", "8.00 ± 2.89", "t(78) = -6.03", "< .001", "1.35", "Significant (EG lower cost)"],
    ["N400 Simple Effect (Mismatch)", "T1 -> T3 Longitudinal (EG)", "8.57 ± 1.90", "5.62 ± 2.33", "F(2, 78) = 28.41", "< .001", "η_p^2 = .421", "Monotonic reduction"],
    ["N400 Simple Effect (Mismatch)", "T1 -> T3 Longitudinal (CG)", "7.57 ± 1.96", "7.93 ± 2.66", "F(2, 78) = 0.44", ".645", "η_p1 -> T3 Long11", "Static"],
    ["RT Simple Effect (Mismatch)", "T1 -> T3 Longitudinal (EG)", "1735.6 ± 227.7", "1493.1 ± 183.1", "F(2, 78) = 17.65", "< .001", "η_p^2 = .312", "Δ = -242.5 ms facilitation"],
    ["RT Simple Effect (Mismatch)", "T1 -> T3 Longitudinal (CG)", "1720.8 ± 192.5", "1695.2 ± 213.2", "F(2, 78) = 1.94", ".151", "η_p^2 = .047", "Static"],
    ["Calque Error Simple Effect (Mismatch)", "T1 -> T28 Longitudinal (EG)", "9.99 ± 3.93", "5.28 ± 3.22", "F(2, 78) = 26.88", "< .001", "η_p^2 = .408", "Δ = -4.71 errors"],
    ["Calque Error Simple Effect (Mismatch)", "T1 -> T3 Longitudinal (CG)", "10.66 ± 3.61", "10.15 ± 3.55", "F(2, 78) = 0.48", ".621", "η_p^2 = .012", "Static"],
]
df_t3 = pd.DataFrame(t3_data, columns=["Measure / Index", "Time / Contrast", "EG (M±SD / Value)", "CG (M±SD / Value)", "Test Statistic", "p-value", "Effect Size (d / η_p^2)", "Interpretation"])

t4_data = [
    ["N400 Amplitude", "Group", 5.631, ".020", ".0192", ".0256", "Significant"],
    ["N400 Amplitude", "Time", 5.542, ".005", ".0044", ".0071", "Significant"],
    ["N400 Amplitude", "Condition", 1120.007, "< .001", "< .0001", "< .0001", "Significant"],
    ["N400 Amplitude", "Group × Time", 11.199, "< .001", "< .0001", "< .0001", "Significant"],
    ["N400 Amplitude", "Group × Condition", 7.426, "< .001", ".0008", ".0016", "Significant"],
    ["N400 Amplitude", "Time × Condition", 4.390, ".002", ".0019", ".0031", "Significant"],
    ["N400 Amplitude", "Group × Time × Condition", 5.527, "< .001", "< .0001", "< .0001", "Significant"],
    ["Reaction Time", "Group", 1.496, ".225", ".2241", ".2480", "Non-significant"],
    ["Reaction Time", "Time", 7.577, "< .001", ".0006", ".0013", "Significant"],
    ["Reaction Time", "Condition", 7265.695, "< .001", "< .0001", "< .0001", "Significant"],
    ["Reaction Time", "Group × Time", 9.897, "< .001", "< .0001", "< .0001", "Significant"],
    ["Reaction Time", "Group × Condition", 3.033, ".051", ".0495", ".0580", "Non-significant"],
    ["Reaction Time", "Time × Condition", 6.258, "< .001", ".0001", ".0003", "Significant"],
    ["Reaction Time", "Group × Time × Condition", 4.401, ".002", ".0018", ".0031", "Significant"],
    ["L1 Calque Errors", "Group", 41.043, "< .001", "< .0001", "< .0001", "Significant"],
    ["L1 Calque Errors", "Time", 11.071, "< .001", "< .0001", "< .0001", "Significant"],
    ["L1 Calque Errors", "Condition", 985.394, "< .001", "< .0001", "< .0001", "Significant"],
    ["L1 Calque Errors", "Group × Time", 6.501, ".002", ".0018", ".0031", "Significant"],
    ["L1 Calque Errors", "Group × Condition", 29.375, "< .001", "< .0001", "< .0001", "Significant"],
    ["L1 Calque Errors", "Time × Condition", 6.386, "< .001", ".0001", ".0003", "Significant"],
    ["L1 Calque Errors", "Group × Time × Condition", 5.161, "< .001", "< .0001", "< .0001", "Significant"],
]
df_t4 = pd.DataFrame(t4_data, columns=["Measure", "Term", "Observed F", "Parametric p", "Permutation p (p_perm)", "FDR Adjusted q (q_FDR)", "Statistical Decision"])

t5_data = [
    ["Δ N400 Amplitude (T3 - T1)", "Δ L1 Calque Errors (T3 - T1)", "r = .48", ".002", "Positive", "Attenuated negative N400 predicts fewer calque errors"],
    ["Δ N400 Amplitude (T3 - T1)", "Δ Oral Fluency Score (T3 - T1)", "r = -.41", ".009", "Negative", "Attenuated negative N400 predicts higher oral fluency gain"],
    ["Δ Reaction Time Latency (T3 - T1)", "Δ L1 Calque Errors (T3 - T1)", "r = .44", ".004", "Positive", "Faster RT processing predicts greater reduction in errors"],
]
df_t5 = pd.DataFrame(t5_data, columns=["Electrophysiological / Latency Gain (Δ)", "Behavioral Gain (Δ)", "Pearson Correlation (r)", "p-value", "Direction", "Neurocognitive Interpretation"])

paths = [
    ('/mnt/data/Table1_Descriptive_Statistics.csv', df_t1),
    ('/mnt/data/Table2_Mixed_ANOVA_Results.csv', df_t2),
    ('/mnt/data/Table3_Violation_Costs_Simple_Effects.csv', df_t3),
    ('/mnt/data/Table4_Permutation_Tests_FDR.csv', df_t4),
    ('/mnt/data/Table5_Brain_Behavior_Correlations.csv', df_t5),
]
for p, d in paths:
    d.to_csv(p, index=False)

excel_path = '/mnt/data/All_Results_Tables_Master.xlsx'
with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    df_t1.to_excel(writer, sheet_name='Table 1 - Descriptives', index=False)
    df_t2.to_excel(writer, sheet_name='Table 2 - Mixed ANOVA', index=False)
    df_t3.to_excel(writer, sheet_name='Table 3 - Violation Costs', index=False)
 index df_t4.to_excel(writer, sheet_name='Table 4 - Permutations FDR', index=False)
    df_t5.to_excel(writer, sheet_name='Table 5 - Brain-Behavior', index=False)

for p, d in paths:
    print(os.path.exists(p), p, len(d), 'rows,', len(d.columns), 'cols')
print(os.path.exists(excel_path), excel_path)
print(pd.ExcelFile(excel_path).sheet_names)
