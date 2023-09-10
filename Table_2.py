# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 07:13:51 2023

@author: Ideal-R
"""

#importing libraries
import pandas as pd
from scipy.stats import norm
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import iqr
import pingouin
#reading the data from excel file
DF = pd.read_excel('Data.xlsx')
lst = [[f'Weight {i} (kg)' for i in ['Pre', '12','48']], [f'BMI {i} (kg/m2)' for i in ['Pre', '12','48']],[f'Fat mass {i} (Kg)' for i in ['Pre', '12','48']], [f'Fat-free mass {i} (kg)' for i in ['Pre', '12','48']],[f'FBS {i} (mg/dL)' for i in ['Pre','12','48']],[f'HbA1c {i} (mg/dL)' for i in ['Pre','12','48']],[f'AST {i} (U/L)' for i in ['Pre','12','48']],[f'ALT {i} (U/L)' for i in ['Pre','12','48']],[f'Exercise min/day {i} (minute)' for i in ['Pre','12','48']]]
dataframe1=[]
dataframe2=[]
dataframe3=[]

index_list = ['Weight (kg)','BMI (kg/m2)','Fat mass (Kg)','Fat-free mass (kg)','FBS (mmol/L)','HbA1c (mg/dL)','AST (U/L)','ALT (U/L)','Exercise min/day (minute)']


for i in range(len(lst)):
    lsti = lst[i]    
    series1 = DF[lsti[1]]
    series2 = DF[lsti[0]]
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
    dataframe1.append({'Mean difference (95% CI)':f'{np.round(mean_difference,decimals=2)} {np.round(confidence_interval,decimals=2)}', 'P-value':f'{stats.ttest_rel(series1,series2).pvalue}'} )
            
    series1 = DF[lsti[2]]
    series2 = DF[lsti[0]]
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
    dataframe2.append({'Mean difference (95% CI)':f'{np.round(mean_difference,decimals=2)} {np.round(confidence_interval,decimals=2)}', 'P-value':f'{stats.ttest_rel(series1,series2).pvalue}'} )
    
    series1 = DF[lsti[2]]
    series2 = DF[lsti[1]]
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
    dataframe3.append({'Mean difference (95% CI)':f'{np.round(mean_difference,decimals=2)} {np.round(confidence_interval,decimals=2)}', 'P-value':f'{stats.ttest_rel(series1,series2).pvalue}'} )
DataFrame1 = pd.DataFrame(dataframe1)
DataFrame2 = pd.DataFrame(dataframe2)
DataFrame3= pd.DataFrame(dataframe3)
DataFrame = pd.concat([DataFrame1,DataFrame2,DataFrame3], axis=1)
DataFrame.index = index_list
print(DataFrame)
DataFrame.to_excel(r"J:\Safavi's project\table_2.xlsx", index=True   )

# ({np.round(confidence_interval,decimals=2)})', 'Median [IQR]':f'{stats.ttest_rel(df[j[0]], df[j[1]]).pvalue}'