# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 00:31:21 2023

@author: Ideal-R
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats


df = pd.read_excel('Data.xlsx')


df_we= df[['Weight Pre (kg)', 'Weight 12 (kg)','Weight 48 (kg)']]
sns.catplot(x='variable', y='value', kind='box', data=pd.melt(df_we),showcaps=False)
sns.stripplot(x='variable', y='value', data=pd.melt(df_we), color='gray', alpha=0.3,zorder=0)
plt.xticks([0, 1, 2], ['Pre','12 month','48 month'])
plt.ylabel('Weight (kg)')
plt.xlabel('')
series2 = df['Weight Pre (kg)']
series1 = df['Weight 12 (kg)']
diff = series2 - series1
        # Calculate mean and standard deviation of the two series
mean1 = np.mean(series1)
mean2 = np.mean(series2)
std1 = np.std(series1, ddof=1)  # Using ddof=1 for sample standard deviation
std2 = np.std(series2, ddof=1)
        # Calculate the standard error of the mean difference
std_error = np.sqrt((std1**2 / len(series1)) + (std2**2 / len(series2)))
        # Calculate the t-score based on the desired confidence level (e.g., 95%)
confidence_level = 0.95
alpha = 1 - confidence_level
di = len(series1) + len(series2) - 2
t_score = stats.t.ppf(1 - alpha / 2, di)
        # Calculate the margin of error
margin_of_error = t_score * std_error
        # Calculate the confidence interval
mean_difference = mean1 - mean2
confidence_interval = (mean_difference - margin_of_error, mean_difference + margin_of_error)
plt.plot([0, 1], [125, 125], color='black', linewidth=0.6)
plt.plot([0, 0], [124, 125], color='black', linewidth=0.6)
plt.plot([1, 1], [124, 125], color='black', linewidth=0.6)
plt.text(0.05, 126, f'{np.round(mean_difference, decimals=2)} {(np.round(confidence_interval,decimals=2))}', fontsize=8)

series2 = df['Weight 12 (kg)']
series1 = df['Weight 48 (kg)']
diff = series2 - series1
        # Calculate mean and standard deviation of the two series
mean1 = np.mean(series1)
mean2 = np.mean(series2)
std1 = np.std(series1, ddof=1)  # Using ddof=1 for sample standard deviation
std2 = np.std(series2, ddof=1)
        # Calculate the standard error of the mean difference
std_error = np.sqrt((std1**2 / len(series1)) + (std2**2 / len(series2)))
        # Calculate the t-score based on the desired confidence level (e.g., 95%)
confidence_level = 0.95
alpha = 1 - confidence_level
di = len(series1) + len(series2) - 2
t_score = stats.t.ppf(1 - alpha / 2, di)
        # Calculate the margin of error
margin_of_error = t_score * std_error
        # Calculate the confidence interval
mean_difference = mean1 - mean2
confidence_interval = (mean_difference - margin_of_error, mean_difference + margin_of_error)
plt.plot([1, 2], [129, 129], color='black', linewidth=0.6)
plt.plot([1, 1], [128, 129], color='black', linewidth=0.6)
plt.plot([2, 2], [128, 129], color='black', linewidth=0.6)
plt.text(1.1, 130, f'{np.round(mean_difference, decimals=2)} {(np.round(confidence_interval,decimals=2))}', fontsize=8)

series2 = df['Weight Pre (kg)']
series1 = df['Weight 48 (kg)']
diff = series2 - series1
        # Calculate mean and standard deviation of the two series
mean1 = np.mean(series1)
mean2 = np.mean(series2)
std1 = np.std(series1, ddof=1)  # Using ddof=1 for sample standard deviation
std2 = np.std(series2, ddof=1)
        # Calculate the standard error of the mean difference
std_error = np.sqrt((std1**2 / len(series1)) + (std2**2 / len(series2)))
        # Calculate the t-score based on the desired confidence level (e.g., 95%)
confidence_level = 0.95
alpha = 1 - confidence_level
di = len(series1) + len(series2) - 2
t_score = stats.t.ppf(1 - alpha / 2, di)
        # Calculate the margin of error
margin_of_error = t_score * std_error
        # Calculate the confidence interval
mean_difference = mean1 - mean2
confidence_interval = (mean_difference - margin_of_error, mean_difference + margin_of_error)
plt.plot([0, 2], [133, 133], color='black', linewidth=0.6)
plt.plot([0, 0], [132, 133], color='black', linewidth=0.6)
plt.plot([2, 2], [132, 133], color='black', linewidth=0.6)
plt.text(0.5, 134, f'{np.round(mean_difference, decimals=2)} {(np.round(confidence_interval,decimals=2))}', fontsize=8)
plt.savefig(r"J:\Safavi's project\figure_1_a.pdf",dpi=300,format="pdf")



df_bmi = df[['BMI Pre (kg/m2)', 'BMI 12 (kg/m2)','BMI 48 (kg/m2)']]
sns.catplot(x='variable', y='value', kind='box', data=pd.melt(df_bmi),showcaps=False)
sns.stripplot(x='variable', y='value', data=pd.melt(df_bmi), color='gray', alpha=0.3,zorder=0)
plt.xticks([0, 1, 2], ['Pre','12 month','48 month'])
plt.ylabel('BMI (kg/m2)')
plt.xlabel('')
plt.savefig(r"J:\Safavi's project\figure_1_b.pdf",dpi=300,format="pdf")




df_fbs = df[['FBS Pre (mg/dL)', 'FBS 12 (mg/dL)','FBS 48 (mg/dL)']]
sns.catplot(x='variable', y='value', kind='box', data=pd.melt(df_fbs),showcaps=False)
sns.stripplot(x='variable', y='value', data=pd.melt(df_fbs), color='gray', alpha=0.3,zorder=0)
plt.xticks([0, 1, 2], ['Pre','12 month','48 month'])
plt.ylabel('FBS (mg/dL)')
plt.xlabel('')
plt.savefig(r"J:\Safavi's project\figure_1_c.pdf",dpi=300,format="pdf")



df_hb = df[['HbA1c Pre (mg/dL)', 'HbA1c 12 (mg/dL)','HbA1c 48 (mg/dL)']]
sns.catplot(x='variable', y='value', kind='box', data=pd.melt(df_hb),showcaps=False)
sns.stripplot(x='variable', y='value', data=pd.melt(df_hb), color='gray', alpha=0.3,zorder=0)
plt.xticks([0, 1, 2], ['Pre','12 month','48 month'])
plt.ylabel('HbA1c (%)')
plt.xlabel('')
plt.savefig(r"J:\Safavi's project\figure_1_d.pdf",dpi=300,format="pdf")


df_exc = df[['Exercise min/day Pre (minute)', 'Exercise min/day 12 (minute)','Exercise min/day 48 (minute)']]
sns.catplot(x='variable', y='value', kind='box', data=pd.melt(df_exc),showcaps=False)
sns.stripplot(x='variable', y='value', data=pd.melt(df_exc), color='gray', alpha=0.3,zorder=0)
plt.xticks([0, 1, 2], ['Pre','12 month','48 month'])
plt.ylabel('Exercise min/day (minute)')
plt.xlabel('')
plt.savefig(r"J:\Safavi's project\figure_1_e.pdf",dpi=300,format="pdf")



df_exc_s = df[['Exercise session/week pre', 'Exercise session/week 12','Exercise session/week 48']]
sns.catplot(x='variable', y='value', kind='box', data=pd.melt(df_exc_s),showcaps=False)
sns.stripplot(x='variable', y='value', data=pd.melt(df_exc_s), color='gray', alpha=0.3,zorder=0)
plt.xticks([0, 1, 2], ['Pre','12 month','48 month'])
plt.ylabel('Exercise session/week')
plt.xlabel('')
plt.savefig(r"J:\Safavi's project\figure_1_f.pdf",dpi=300,format="pdf")

plt.show()

