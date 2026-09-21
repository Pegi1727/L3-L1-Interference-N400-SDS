import pandas as pd
import os

t1_data = [
    ["N400 Amplitude (uV)", "CG", "T1", "2.81 | 1.00", "3.59 | 1.05", "7.57 | 1.96"],
    ["N400 Amplitude (uV)", "CG", "T2", "3.14 | 1.15", "3.53 | 1.13", "7.87 | 2.18"],
    ["N400 Amplitude (uV)", "CG", "T3", "3.08 | 1.08", "3.68 | 1.05", "7.93 | 2.66"],
    ["N400 Amplitude (uV)", "EG", "T1", "3.38 | 1.25", "3.69 | 1.26", "8.57 | 1.90"],
    ["N400 Amplitude (uV)", "EG", "T2", "2.77 | 1.10", "3.31 | 1.13", "6.58 | 2.27"],
    ["N400 Amplitude (uV)", "EG", "T3", "2.36 | 0.99", "2.63 | 0.97", "5.62 | 2.33"],
    ["Reaction Time (ms)", "CG", "T1", "668.0 | 101.4", "905.7 | 124.9", "1720.8 | 192.5"],
    ["Reaction Time (ms)", "CG", "T2", "643.9 | 95.8", "880.8 | 109.9", "1624.8 | 207.6"],
    ["Reaction Time (ms)", "CG", "T3", "668.6 | 106.6", "895.8 | 116.8", "1695.2 | 213.2"],
    ["Reaction Time (ms)", "EG", "T1", "687.2 | 117.8", "906.9 | 128.8", "1735.6 | 227.7"],
    ["Reaction Time (ms)", "EG", "T2", "683.9 | 115.1", "897.4 | 104.9", "1678.1 | 232.4"],
    ["Reaction Time (ms)", "EG", "T3", "598.1 | 88.0", "760.3 | 113.6", "1493.1 | 183.1"],
    ["Oral Fluency (Score)", "CG", "T1", "11.00 | 2.01", "10.15 | 2.05", "4.48 | 1.22"],
    ["Oral Fluency (Score)", "CG", "T2", "11.08 | 1.98", "10.05 | 1.88", "4.40 | 1.22"],
    ["Oral Fluency (Score)", "CG", "T3", "11.20 | 2.08", "10.22 | 1.83", "4.45 | 1.15"],
    ["Oral Fluency (Score)", "EG", "T1", "10.68 | 2.04", "9.92 | 2.21", "4.08 | 1.07"],
    ["Oral Fluency (Score)", "EG", "T2", "11.60 | 1.96", "10.65 | 1.83", "4.68 | 1.31"],
    ["Oral Fluency (Score)", "EG", "T3", "12.18 | 1.96", "11.20 | 1.84", "5.30 | 1.45"],
    ["L1 Pragmatic Reliance", "CG", "T1", "2.38 | 1.05", "3.58 | 1.24", "8.05 | 1.77"],
    ["L1 Pragmatic Reliance", "CG", "T2", "2.22 | 0.97", "3.45 | 1.15", ".02 | 11.62"],
    ["L1 Pragmatic Reliance", "CG", "T3", "2.12 | 0.88", "3.35 | 1.10", "8.05 | 1.58"],
    ["L1 Pragmatic Reliance", "EG", "T1", "2.60 | 0.96", "3.80 | 1.30", "8.65 | 1.66"],
    ["L1 Pragmatic Reliance", "EG", "T2", "2.15 | 1.03", "3.15 | 1.27", "7.78 | 1.87"],
    ["L1 Pragmatic Reliance", "EG", "T3", "1.72 | 0.82", "2.62 | 1.03", "6.48 | 1.91"],
    ["L1 Calque Errors", "CG", "T1", "2.03 | 1.19", "3.97 | 1.89", "10.66 | 3.61"],
    ["L1 Calque Errors", "CG", "T2", "2.12 | 1.34", "3.90 | 1.84", "10.14 | 3.55"],
    ["L1 Calque Errors", "CG", "T3", "2.15 | 1.37", "3.89 | 1.80", "10.15 | 3.55"],
    ["L1 Calque Errors", "EG", "T1", "2.07 | 1.19", "4.00 | 1.85", "9.99 | 3.93"],
    ["L1 Calque Errors", "EG", "T2", "1.52 | 1.18", "2.95 | 1.58", "7.48 | 3.25"],
    ["L1 Calque Errors", "EG", "T3", "1.02 | 0.97", "1.98 | 1.37", "5.28 | 3.22"],
]
PM = "\u00b1"
for row in t1_data:
    for i in (3, 4, 5):
        row[i] = row[i].replace(" | ", " " + PM + " ")
df_t1 = pd.DataFrame(t1_data, columns=["Measure", "Group", "Time", "Control (M" + PM + "SD)", "Target (M" + PM + "SD)", "Mismatch (M" + PM + "SD)"])
df_t1.to_csv("/mnt/data/part_t1.csv", index=False)
print("part_t1 ok", df_t1.shape)
