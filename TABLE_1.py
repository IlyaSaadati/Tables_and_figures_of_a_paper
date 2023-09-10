# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 23:35:59 2023

@author: Ideal-R
"""

#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import iqr

#reading the data from excel file
df = pd.read_excel('Data.xlsx')
lst = [[f'Weight {i} (kg)' for i in ['Pre', '12','48']], [f'BMI {i} (kg/m2)' for i in ['Pre', '12','48']],[f'Fat mass {i} (Kg)' for i in ['Pre', '12','48']], [f'Fat-free mass {i} (kg)' for i in ['Pre', '12','48']],[f'Excess weight loss {i} (%)' for i in ['12','48']],[f'FBS {i} (mg/dL)' for i in ['Pre','12','48']],[f'HbA1c {i} (mg/dL)' for i in ['Pre','12','48']],[f'AST {i} (U/L)' for i in ['Pre','12','48']],[f'ALT {i} (U/L)' for i in ['Pre','12','48']],[f'Exercise min/day {i} (minute)' for i in ['Pre','12','48']],[f'Exercise session/week {i}' for i in ['pre','12','48']]]
dataframe1=[]
dataframe2=[]
dataframe3=[]
index_list=['Weight (kg)','BMI (kg/m2)','Fat mass (Kg)','Fat-free mass (kg)','Loss of excess body weight (LEBW) (%)','FBS (mmol/L)','HbA1c (mg/dL)','AST (U/L)','ALT (U/L)','Exercise minute /day','Exercise session/week','Exercise type (Aerobic)','Exercise type (Aerobic & Strength)','Exercise intensity (Low)','Exercise intensity (Moderate)']
t=0
for j in lst:
   
    t+=1
    
    if len(j)==3:   
         # print(np.mean(df[i]))
         dataframe1.append({'Mean (SD)no./No. (%)':f'{np.round(np.mean(df[j[0]]),decimals=2)} ({np.round(np.std(df[j[0]]),decimals=2)})', 'Median [IQR]':f'{np.round(np.median(df[j[0]]),decimals=2)} [{np.round(np.quantile(df[j[0]], .25),decimals=2)},{np.round(np.quantile(df[j[0]], .75),decimals=2)}]'})
         dataframe2.append({'Mean (SD)no./No. (%)':f'{np.round(np.mean(df[j[1]]),decimals=2)} ({np.round(np.std(df[j[1]]),decimals=2)})', 'Median [IQR]':f'{np.round(np.median(df[j[1]]),decimals=2)} [{np.round(np.quantile(df[j[1]], .25),decimals=2)},{np.round(np.quantile(df[j[1]], .75),decimals=2)}]'})
         dataframe3.append({'Mean (SD)no./No. (%)':f'{np.round(np.mean(df[j[2]]),decimals=2)} ({np.round(np.std(df[j[2]]),decimals=2)})', 'Median [IQR]':f'{np.round(np.median(df[j[2]]),decimals=2)} [{np.round(np.quantile(df[j[2]], .25),decimals=2)},{np.round(np.quantile(df[j[2]], .75),decimals=2)}]'})
    elif len(j)==2:     
         dataframe1.append({'Mean (SD)no./No. (%)':'', 'Median [IQR]':''})

         dataframe2.append({'Mean (SD)no./No. (%)':f'{np.round(np.mean(df[j[0]]),decimals=2)} ({np.round(np.std(df[j[0]]),decimals=2)})', 'Median [IQR]':f'{np.round(np.median(df[j[0]]),decimals=2)} [{np.round(np.quantile(df[j[0]], .25),decimals=2)},{np.round(np.quantile(df[j[0]], .75),decimals=2)}]'})
         dataframe3.append({'Mean (SD)no./No. (%)':f'{np.round(np.mean(df[j[1]]),decimals=2)} ({np.round(np.std(df[j[1]]),decimals=2)})', 'Median [IQR]':f'{np.round(np.median(df[j[1]]),decimals=2)} [{np.round(np.quantile(df[j[1]], .25),decimals=2)},{np.round(np.quantile(df[j[1]], .75),decimals=2)}]'})

# lst_ae = [f'Exersice type {i}' for i in ['Pre', '12','48']]
n= df.shape[0]
count1=df['Exersice type Pre'].value_counts()
count2=df['Exersice type 12'].value_counts()
count3=df['Exersice type 48'].value_counts()
dataframe1.append({'Mean (SD)no./No. (%)':f'{count1[1]} ({np.round(count1[1]/n*100, decimals=2)}%)', 'Median [IQR]':''})
dataframe2.append({'Mean (SD)no./No. (%)':f'{count1[1]} ({np.round(count1[1]/n*100, decimals=2)}%)', 'Median [IQR]':''})
dataframe3.append({'Mean (SD)no./No. (%)':f'{count1[1]} ({np.round(count1[1]/n*100, decimals=2)}%)', 'Median [IQR]':''})
dataframe1.append({'Mean (SD)no./No. (%)':f'{count1[2]} ({np.round(count1[2]/n*100, decimals=2)}%)', 'Median [IQR]':''})
dataframe2.append({'Mean (SD)no./No. (%)':f'{count1[2]} ({np.round(count1[2]/n*100, decimals=2)}%)', 'Median [IQR]':''})
dataframe3.append({'Mean (SD)no./No. (%)':f'{count1[2]} ({np.round(count1[2]/n*100, decimals=2)}%)', 'Median [IQR]':''})

count1=df['Exercise intensity pre'].value_counts()
count2=df['Exercise intensity 12'].value_counts()
count3=df['Exercise intensity 48'].value_counts()
dataframe1.append({'Mean (SD)no./No. (%)':f'{count1[1]} ({np.round(count1[1]/n*100, decimals=2)}%)', 'Median [IQR]':''})
dataframe2.append({'Mean (SD)no./No. (%)':f'{count1[1]} ({np.round(count1[1]/n*100, decimals=2)}%)', 'Median [IQR]':''})
dataframe3.append({'Mean (SD)no./No. (%)':f'{count1[1]} ({np.round(count1[1]/n*100, decimals=2)}%)', 'Median [IQR]':''})
dataframe1.append({'Mean (SD)no./No. (%)':f'{count1[2]} ({np.round(count1[2]/n*100, decimals=2)}%)', 'Median [IQR]':''})
dataframe2.append({'Mean (SD)no./No. (%)':f'{count1[2]} ({np.round(count1[2]/n*100, decimals=2)}%)', 'Median [IQR]':''})
dataframe3.append({'Mean (SD)no./No. (%)':f'{count1[2]} ({np.round(count1[2]/n*100, decimals=2)}%)', 'Median [IQR]':''})

DataFrame1 = pd.DataFrame(dataframe1)
DataFrame2 = pd.DataFrame(dataframe2)
DataFrame3= pd.DataFrame(dataframe3)
DataFrame = pd.concat([DataFrame1,DataFrame2,DataFrame3], axis=1)
DataFrame.index = index_list
print(DataFrame)
DataFrame.to_excel(r"J:\Safavi's project\table_1.xlsx", index=True   )
