# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 01:27:47 2023

@author: Ideal-R
"""

#importing libraries
import pandas as pd
import pingouin

import numpy as np
from scipy.stats import iqr
import scipy.stats as stats
#reading the data from excel file
DF = pd.read_excel('Data.xlsx')

df_in = DF[DF['Excess weight loss 48 (%)']<50]
df_su = DF[DF['Excess weight loss 48 (%)']>=50]

lst = [['Age (years)','Height (m)'],[f'Weight {i} (kg)' for i in ['Pre', '12','48']], [f'BMI {i} (kg/m2)' for i in ['Pre', '12','48']],[f'Fat mass {i} (Kg)' for i in ['Pre', '12','48']], [f'Fat-free mass {i} (kg)' for i in ['Pre', '12','48']],[f'Excess weight loss {i} (%)' for i in ['12','48']],[f'FBS {i} (mg/dL)' for i in ['Pre','12','48']],[f'HbA1c {i} (mg/dL)' for i in ['Pre','12','48']],[f'Exercise min/day {i} (minute)' for i in ['Pre','12','48']],[f'Exercise session/week {i}' for i in ['pre','12','48']]]

dataframe = []
index_list = []
for j in lst:
    for i in j:
        index_list.append(i) 
        series1 = df_in[i]
        series2 = df_su[i]
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
        df = len(series1) + len(series2) - 2
        t_score = stats.t.ppf(1 - alpha / 2, df)
                # Calculate the margin of error
        margin_of_error = t_score * std_error
                # Calculate the confidence interval
        mean_difference = mean1 - mean2
        confidence_interval = (mean_difference - margin_of_error, mean_difference + margin_of_error)
           
             # print(np.mean(df[i]))
        dataframe.append({'Insufficient Response':f'{np.round(np.mean(df_in[i]),decimals=2)} ({np.round(np.std(df_in[i],ddof=1),decimals=2)})', 'Good Response':f'{np.round(np.mean(df_su[i]),decimals=2)} ({np.round(np.std(df_su[i],ddof=1),decimals=2)})','P-value':f'{stats.ttest_ind(df_su[i],df_in[i]).pvalue}', 'Mean Difference (95%CI)':f'{np.round(mean_difference,decimals=2)} {np.round(confidence_interval,decimals=2)}'})
        #      dataframe2.append({'Mean (SD)no./No. (%)':f'{np.round(np.mean(df[j[1]]),decimals=2)} ({np.round(np.std(df[j[1]]),decimals=2)})', 'Median [IQR]':f'{np.round(np.median(df[j[1]]),decimals=2)} [{np.round(np.quantile(df[j[1]], .25),decimals=2)},{np.round(np.quantile(df[j[1]], .75),decimals=2)}]'})
        #      dataframe3.append({'Mean (SD)no./No. (%)':f'{np.round(np.mean(df[j[2]]),decimals=2)} ({np.round(np.std(df[j[2]]),decimals=2)})', 'Median [IQR]':f'{np.round(np.median(df[j[2]]),decimals=2)} [{np.round(np.quantile(df[j[2]], .25),decimals=2)},{np.round(np.quantile(df[j[2]], .75),decimals=2)}]'})
        # elif len(j)==2:     
        #      dataframe1.append({'Mean (SD)no./No. (%)':'', 'Median [IQR]':''})
    
        #      dataframe2.append({'Mean (SD)no./No. (%)':f'{np.round(np.mean(df[j[0]]),decimals=2)} ({np.round(np.std(df[j[0]]),decimals=2)})', 'Median [IQR]':f'{np.round(np.median(df[j[0]]),decimals=2)} [{np.round(np.quantile(df[j[0]], .25),decimals=2)},{np.round(np.quantile(df[j[0]], .75),decimals=2)}]'})
        #      dataframe3.append({'Mean (SD)no./No. (%)':f'{np.round(np.mean(df[j[1]]),decimals=2)} ({np.round(np.std(df[j[1]]),decimals=2)})', 'Median [IQR]':f'{np.round(np.median(df[j[1]]),decimals=2)} [{np.round(np.quantile(df[j[1]], .25),decimals=2)},{np.round(np.quantile(df[j[1]], .75),decimals=2)}]'})
n_in= df_in.shape[0]
n_su= df_su.shape[0]

counti1=df_in['Exersice type Pre'].value_counts()
counti2=df_in['Exersice type 12'].value_counts()
counti3=df_in['Exersice type 48'].value_counts()
counts1=df_su['Exersice type Pre'].value_counts()
counts2=df_su['Exersice type 12'].value_counts()
counts3=df_su['Exersice type 48'].value_counts()
index_list.append('Exersice type Pre (Aerobic)')
index_list.append('Exersice type Pre (Aerobic & Strenght)')
index_list.append('Exersice type 12 (Aerobic)')
index_list.append('Exersice type 12 (Aerobic & Strenght)')
index_list.append('Exersice type 48 (Aerobic)')
index_list.append('Exersice type 48 (Aerobic & Strenght)')
dataframe.append({'Insufficient Response':f'{counti1[1]} ({np.round(counti1[1]/n_in*100, decimals=2)}%)', 'Good Response':f'{counts1[1]} ({np.round(counts1[1]/n_su*100, decimals=2)}%)','P-value':f'{stats.ttest_ind(df_in["Exersice type Pre"],df_su["Exersice type Pre"]).pvalue}','Mean Difference (95%CI)':''})
dataframe.append({'Insufficient Response':f'{counti1[2]} ({np.round(counti1[2]/n_in*100, decimals=2)}%)', 'Good Response':f'{counts1[2]} ({np.round(counts1[2]/n_su*100, decimals=2)}%)','P-value':'','Mean Difference (95%CI)':''})
    
dataframe.append({'Insufficient Response':f'{counti2[1]} ({np.round(counti2[1]/n_in*100, decimals=2)}%)', 'Good Response':f'{counts2[1]} ({np.round(counts2[1]/n_su*100, decimals=2)}%)','P-value':f'{stats.ttest_ind(df_in["Exersice type 12"],df_su["Exersice type 12"]).pvalue}','Mean Difference (95%CI)':''})
dataframe.append({'Insufficient Response':'0 (0.0%)', 'Good Response':f'{counts2[2]} ({np.round(counts2[2]/n_su*100, decimals=2)}%)','P-value':'','Mean Difference (95%CI)':''})
    
dataframe.append({'Insufficient Response':f'{counti3[1]} ({np.round(counti3[1]/n_in*100, decimals=2)}%)', 'Good Response':f'{counts3[1]} ({np.round(counts3[1]/n_su*100, decimals=2)}%)','P-value':f'{stats.ttest_ind(df_in["Exersice type 48"],df_su["Exersice type 48"]).pvalue}','Mean Difference (95%CI)':''})
dataframe.append({'Insufficient Response':'0 (0.0%)', 'Good Response':f'{counts3[2]} ({np.round(counts3[2]/n_su*100, decimals=2)}%)','P-value':'','Mean Difference (95%CI)':''})

    
DataFrame=pd.DataFrame(dataframe)
DataFrame.index =index_list

print(DataFrame)
DataFrame.to_excel(r"J:\Safavi's project\table_3.xlsx", index=True   )

# , 'P-value':f'{pingouin.ttest(df_in, df_su,paired=False)["p-val"]}'