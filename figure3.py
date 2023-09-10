# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 02:35:56 2023

@author: Ideal-R
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_excel('Data.xlsx')


sns.stripplot(data = df[df['Exercise min/day 12 (minute)']<=45], x= 'Exercise min/day 12 (minute)', y='Excess weight loss 12 (%)', alpha=0.6, color='black')
plt.savefig(r"F:\Safavi's project\figure_3_a.pdf",dpi=300,format="pdf")

plt.show()

sns.stripplot(data = df, x= 'Exercise min/day 48 (minute)', y='Excess weight loss 48 (%)',alpha=0.6, color='black')
plt.savefig(r"F:\Safavi's project\figure_3_b.pdf",dpi=300,format="pdf")

plt.show()

g=sns.stripplot(data = df, x= 'HbA1c 12 (mg/dL)', y='Excess weight loss 12 (%)', alpha=0.6, color='black')

plt.savefig(r"F:\Safavi's project\figure_3_c.pdf",dpi=300,format="pdf")



plt.show()

axs=sns.stripplot(data = df, x= 'HbA1c 48 (mg/dL)', y='Excess weight loss 48 (%)', alpha=0.6, color='black')
plt.savefig(r"F:\Safavi's project\figure_3_d.pdf",dpi=300,format="pdf")


plt.show()