# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 13:41:45 2023

@author: Ideal-R
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np



DF = pd.read_excel('Data.xlsx')
DF['Response 12 (BMI 25% Drop)']=np.zeros(shape=DF.shape[0]) 
DF['legends']=np.array(None) 
for i in range(DF.shape[0]):  
    if ((DF.iloc[i,41]*7 < 150) & (DF.iloc[i,42]*7<150)):
        DF.iloc[i,51]= 'less than 150 minutes in both 12 and 48 months'
    
    if((DF.iloc[i,41]*7 > 150) | (DF.iloc[i,42]*7>150)):
        DF.iloc[i,51]='more than 150 minutes in either 12 or 48 months'
    
    if ((DF.iloc[i,41]*7 > 150) & (DF.iloc[i,42]*7>150)):
        DF.iloc[i,51]= 'more than 150 minutes in both 12 and 48 months'
        
for i in range(DF.shape[0]):
    
    if DF.iloc[i, 10]/DF.iloc[i, 9] <= 0.75: 
        DF.iloc[i,50] = 'Good'
    else:
        DF.iloc[i,50] = 'Insufficient'

axs=sns.countplot(x='Response 12 (BMI 25% Drop)', data=DF,hue='legends')
custom_ylim = (0, 250)
plt.setp(axs,ylim=custom_ylim)
plt.savefig(r"F:\Safavi's project\figure_s1.pdf",dpi=300,format="pdf")

plt.show()


DF = pd.read_excel('Data.xlsx')
DF['Response 48 (BMI 25% Drop)']=np.zeros(shape=DF.shape[0]) 
DF['legends']=np.array(None) 
for i in range(DF.shape[0]):  
    if ((DF.iloc[i,41]*7 < 150) & (DF.iloc[i,42]*7<150)):
        DF.iloc[i,51]= 'less than 150 minutes in both 12 and 48 months'
    if((DF.iloc[i,41]*7 > 150) | (DF.iloc[i,42]*7>150)):
        DF.iloc[i,51]='more than 150 minutes in either 12 or 48 months'
    if ((DF.iloc[i,41]*7 > 150) & (DF.iloc[i,42]*7>150)):
        DF.iloc[i,51]= 'more than 150 minutes in both 12 and 48 months'
for i in range(DF.shape[0]):
    
    if DF.iloc[i, 11]/DF.iloc[i, 9] <= 0.75: 
        DF.iloc[i,50] = 'Good'
    else:
        DF.iloc[i,50] = 'Insufficient'
axs = sns.countplot(x='Response 48 (BMI 25% Drop)', data=DF,hue='legends')
custom_ylim = (0, 250)
plt.setp(axs,ylim=custom_ylim)
plt.savefig(r"F:\Safavi's project\figure_s2.pdf",dpi=300,format="pdf")

plt.show()


DF = pd.read_excel('Data.xlsx')
DF['Response 12 (LEBW 50% )']=np.zeros(shape=DF.shape[0]) 
DF['legends']=np.array(None) 
for i in range(DF.shape[0]):  
    if ((DF.iloc[i,41]*7 < 150) & (DF.iloc[i,42]*7<150)):
        DF.iloc[i,51]= 'less than 150 minutes in both 12 and 48 months'
    if((DF.iloc[i,41]*7 > 150) | (DF.iloc[i,42]*7>150)):
        DF.iloc[i,51]='more than 150 minutes in either 12 or 48 months'
    if ((DF.iloc[i,41]*7 > 150) & (DF.iloc[i,42]*7>150)):
        DF.iloc[i,51]= 'more than 150 minutes in both 12 and 48 months'
for i in range(DF.shape[0]):
    
    if DF.iloc[i, 18] >= 50: 
        DF.iloc[i,50] = 'Good'
    else:
        DF.iloc[i,50] = 'Insufficient'
axs = sns.countplot(x='Response 12 (LEBW 50% )', data=DF,hue='legends')
custom_ylim = (0, 250)
plt.setp(axs,ylim=custom_ylim)
plt.savefig(r"F:\Safavi's project\figure_s3.pdf",dpi=300,format="pdf")

plt.show()


DF = pd.read_excel('Data.xlsx')
DF['Response 48 (LEBW 50% )']=np.zeros(shape=DF.shape[0]) 
DF['legends']=np.array(None) 
for i in range(DF.shape[0]):  
    if ((DF.iloc[i,41]*7 < 150) & (DF.iloc[i,42]*7<150)):
        DF.iloc[i,51]= 'less than 150 minutes in both 12 and 48 months'
    if((DF.iloc[i,41]*7 > 150) | (DF.iloc[i,42]*7>150)):
        DF.iloc[i,51]='more than 150 minutes in either 12 or 48 months'
    if ((DF.iloc[i,41]*7 > 150) & (DF.iloc[i,42]*7>150)):
        DF.iloc[i,51]= 'more than 150 minutes in both 12 and 48 months'
for i in range(DF.shape[0]):
    
    if DF.iloc[i, 20] >= 50: 
        DF.iloc[i,50] = 'Good'
    else:
        DF.iloc[i,50] = 'Insufficient'
axs = sns.countplot(x='Response 48 (LEBW 50% )', data=DF,hue='legends')
custom_ylim = (0, 250)
plt.setp(axs,ylim=custom_ylim)
plt.savefig(r"F:\Safavi's project\figure_s4.pdf",dpi=300,format="pdf")

plt.show()

