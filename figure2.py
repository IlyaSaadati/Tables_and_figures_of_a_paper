# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 02:35:36 2023

@author: Ideal-R
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats


df = pd.read_excel('Data.xlsx')

df2=df[(df['Exercise min/day Pre (minute)']<30) & (df['HbA1c Pre (mg/dL)']<7.5)]
sns.stripplot(data = df2, x= 'Exercise min/day Pre (minute)', y='HbA1c Pre (mg/dL)', alpha=0.6, color='black')
corr_coef, p_value = stats.pearsonr(df2['Exercise min/day Pre (minute)'], df2['HbA1c Pre (mg/dL)'])
plt.text(0.05, 7, f'R={np.round(corr_coef,decimals=3)}, {np.round(p_value,decimals=1)}', fontsize=12)
plt.savefig(r"J:\Safavi's project\figure_2_a.pdf",dpi=300,format="pdf")

plt.show()

df3=df[df['Exercise min/day 12 (minute)']<50]
sns.stripplot(data = df3, x= 'Exercise min/day 12 (minute)', y='HbA1c 12 (mg/dL)', alpha=0.6, color='black')
corr_coef, p_value = stats.pearsonr(df3['Exercise min/day 12 (minute)'], df3['HbA1c 12 (mg/dL)'])
plt.text(0.05, 5.5, f'R={np.round(corr_coef,decimals=2)}, {np.round(p_value,decimals=3)}', fontsize=12)
plt.savefig(r"J:\Safavi's project\figure_2_b.pdf",dpi=300,format="pdf")

plt.show()



sns.stripplot(data = df, x= 'Exercise min/day 48 (minute)', y='HbA1c 48 (mg/dL)', alpha=0.6, color='black')
plt.savefig(r"J:\Safavi's project\figure_2_c.pdf",dpi=300,format="pdf")

plt.show()


df4=df[(df['Exercise min/day Pre (minute)']<25) & (df['FBS Pre (mg/dL)']<200)]
sns.stripplot(data = df4, x= 'Exercise min/day Pre (minute)', y='FBS Pre (mg/dL)', alpha=0.6, color='black')
plt.savefig(r"J:\Safavi's project\figure_2_d.pdf",dpi=300,format="pdf")

plt.show()


EF12=sns.stripplot(data = df, x= 'Exercise min/day 12 (minute)', y='FBS 12 (mg/dL)', alpha=0.6, color='black')
# EF12.set(xlim=(0, 40))
#plt.xticks([10,20,30,40])
plt.savefig(r"J:\Safavi's project\figure_2_e.pdf",dpi=300,format="pdf")

plt.show()
EF48=sns.stripplot(data = df, x= 'Exercise min/day 48 (minute)', y='FBS 48 (mg/dL)', alpha=0.6, color='black')
# EF48.set(xlim=(0, 40))
#plt.xticks([20,30,40])


plt.savefig(r"J:\Safavi's project\figure_2_f.pdf",dpi=300,format="pdf")

plt.show()

