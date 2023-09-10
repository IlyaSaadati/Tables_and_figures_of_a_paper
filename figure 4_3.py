# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 06:49:39 2023

@author: Ideal-R
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 06:44:58 2023

@author: Ideal-R
"""
#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


#reading the data from excel file
df = pd.read_excel('Data.xlsx')



# plot 2-1
df.loc[(df['Exercise session/week pre']==5) |(df['Exercise session/week pre']==6), 'Exercise session/week pre'] = '5-6 session'
df.loc[(df['Exercise session/week pre']==4) |(df['Exercise session/week pre']==3), 'Exercise session/week pre'] = '3-4 session'
df.loc[(df['Exercise session/week pre']==2) | (df['Exercise session/week pre']==1), 'Exercise session/week pre'] = '1-2 session'
box_plot=sns.boxplot(x='Exercise session/week pre', y='Excess weight loss 48 (%)', data=df,showcaps=False,palette='GnBu')
sns.stripplot(x='Exercise session/week pre', y='Excess weight loss 48 (%)', data=df, color='black', alpha=0.1,zorder=0)
plt.xlabel('Exercise session')
plt.ylabel('Loss of Excess Body Weight (%)')
box_plot.spines['top'].set_visible(False)
box_plot.spines['right'].set_visible(False) 
plt.yticks(np.arange(0, 150, step=50))  # Set label locations.
# plt.xticks([0, 1, ], ['Low', 'Moderate'])
# adding texts to boxes which represent number of data in each box
counts = df['Exercise session/week pre'].value_counts()
print(counts)
plt.text(-0.07, 130, f'N={counts["1-2 session"]}', fontsize=8)
plt.text(0.9, 140, f'N={counts["3-4 session"]}', fontsize=8)
plt.text(1.9, 100, f'N={counts["5-6 session"]}', fontsize=8)
plt.savefig(r"F:\Safavi's project\figure_4_3_a.pdf",dpi=300,format="pdf")

plt.show()

#plot 2-2

# creating subdata we need to work on
df1 = df[df['Exercise session/week pre']=="1-2 session"]
df2 = df[df['Exercise session/week pre']=="3-4 session"]
df3= df[df['Exercise session/week pre']=="5-6 session"]

# melting dataframes
md1 = df1.melt(value_vars=['BMI Pre (kg/m2)', 'BMI 48 (kg/m2)'])
md2 = df2.melt(value_vars=['BMI Pre (kg/m2)', 'BMI 48 (kg/m2)'])
md3= df3.melt(value_vars=['BMI Pre (kg/m2)', 'BMI 48 (kg/m2)'])
mdf = df.melt(value_vars=['BMI Pre (kg/m2)', 'BMI 48 (kg/m2)'])

# main plot
fig, axs = plt.subplots(1, 4, figsize=(10, 5), sharey=False)
# determining  ylim to have same ylim in future subpplots
max_ylim = float(np.max(mdf['value']))+1
min_ylim=float(np.min(mdf['value']))-1
custom_ylim = (min_ylim, max_ylim)
plt.setp(axs,ylim=custom_ylim)


# Create the first boxplot
sns.boxplot(y='value',x='variable',data=md1, ax=axs[0],showcaps=False)
sns.stripplot(y='value',x='variable',data=md1, ax=axs[0], color='black', alpha=0.1,zorder=0)
axs[0].spines['right'].set_visible(False)
# axs[0].set_title('Boxplot 1')
axs[0].title.set_text("1-2 session")
axs[0].set_xlabel('')
axs[0].set_ylabel('BMI (kg/m2)')
axs[0].set_yticks(np.arange(30, 60, step=10))

axs[0].set_xticks([0, 1], ['Pre', '48 months'])


# Create the second boxplot
sns.boxplot(y='value',x='variable',data=md2, ax=axs[1],showcaps=False)
sns.stripplot(y='value',x='variable',data=md2, ax=axs[1], color='black', alpha=0.1,zorder=0)
axs[1].spines['right'].set_visible(False)
axs[1].spines['left'].set_visible(False)
axs[1].set_title("3-4 session")
axs[1].set_xlabel('')
axs[1].set_ylabel('')
axs[1].set_yticks(np.arange(30, 60, step=10))
axs[1].set_yticks([]) # used to make yticks invisible
axs[1].set_xticks([0, 1], ['Pre', '48 months'])

# Create the third boxplot

sns.boxplot(y='value',x='variable',data=md3, ax=axs[2],showcaps=False)
sns.stripplot(y='value',x='variable',data=md3, ax=axs[2], color='black', alpha=0.1,zorder=0)
axs[2].set_title("5-6 session")
axs[2].set_xlabel('')
axs[2].set_xticks([0, 1], ['Pre', '48 months'])
axs[2].set_yticks(np.arange(30, 60, step=10))
axs[2].set_ylabel('')
axs[2].set_yticks([])
axs[2].spines['left'].set_visible(False)
axs[2].spines['right'].set_visible(False)


sns.boxplot(y='value',x='variable',data=mdf, ax=axs[3],showcaps=False)
sns.stripplot(y='value',x='variable',data=mdf, ax=axs[3], color='black', alpha=0.1,zorder=0)
axs[3].set_title('(all)')
axs[3].set_xlabel('')
axs[3].set_xticks([0, 1], ['Pre', '48 months'])
axs[3].set_yticks(np.arange(30, 60, step=10))
axs[3].set_ylabel('')
axs[3].set_yticks([])
axs[3].spines['left'].set_visible(False)
axs[3].spines['right'].set_visible(False)
# Adjust layout
plt.tight_layout()
plt.savefig(r"F:\Safavi's project\figure_4_3_b.pdf",dpi=300,format="pdf")

# Show the merged boxplots
plt.show()


# plot 2-3

df1 = df[df['Exercise session/week pre']=="1-2 session"]
df2 = df[df['Exercise session/week pre']=="3-4 session"]
df3= df[df['Exercise session/week pre']=="5-6 session"]

# melting dataframes
md1 = df1.melt(value_vars=['HbA1c Pre (mg/dL)', 'HbA1c 48 (mg/dL)'])
md2 = df2.melt(value_vars=['HbA1c Pre (mg/dL)', 'HbA1c 48 (mg/dL)'])
md3= df3.melt(value_vars=['HbA1c Pre (mg/dL)', 'HbA1c 48 (mg/dL)'])
mdf = df.melt(value_vars=['HbA1c Pre (mg/dL)', 'HbA1c 48 (mg/dL)'])

# main plot
fig, axs = plt.subplots(1, 4, figsize=(10, 5), sharey=False)
# determining  ylim to have same ylim in future subpplots
max_ylim = float(np.max(mdf['value']))+1
min_ylim=float(np.min(mdf['value']))-1
custom_ylim = (min_ylim, max_ylim)
plt.setp(axs,ylim=custom_ylim)


# Create the first boxplot
sns.boxplot(y='value',x='variable',data=md1, ax=axs[0],showcaps=False)
sns.stripplot(y='value',x='variable',data=md1, ax=axs[0], color='black', alpha=0.1,zorder=0)
axs[0].spines['right'].set_visible(False)
# axs[0].set_title('Boxplot 1')
axs[0].title.set_text("1-2 session")
axs[0].set_xlabel('')
axs[0].set_ylabel('BMI (kg/m2)')
axs[0].set_yticks(np.arange(4, 10, step=2))

axs[0].set_xticks([0, 1], ['Pre', '48 months'])


# Create the second boxplot
sns.boxplot(y='value',x='variable',data=md2, ax=axs[1],showcaps=False)
sns.stripplot(y='value',x='variable',data=md2, ax=axs[1], color='black', alpha=0.1,zorder=0)
axs[1].spines['right'].set_visible(False)
axs[1].spines['left'].set_visible(False)
axs[1].set_title("3-4 session")
axs[1].set_xlabel('')
axs[1].set_ylabel('')
axs[1].set_yticks(np.arange(4, 10, step=2))
axs[1].set_yticks([]) # used to make yticks invisible
axs[1].set_xticks([0, 1], ['Pre', '48 months'])

# Create the third boxplot

sns.boxplot(y='value',x='variable',data=md3, ax=axs[2],showcaps=False)
sns.stripplot(y='value',x='variable',data=md3, ax=axs[2], color='black', alpha=0.1,zorder=0)
axs[2].set_title("5-6 session")
axs[2].set_xlabel('')
axs[2].set_xticks([0, 1], ['Pre', '48 months'])
axs[2].set_yticks(np.arange(4, 10, step=2))
axs[2].set_ylabel('')
axs[2].set_yticks([])
axs[2].spines['left'].set_visible(False)
axs[2].spines['right'].set_visible(False)


sns.boxplot(y='value',x='variable',data=mdf, ax=axs[3],showcaps=False)
sns.stripplot(y='value',x='variable',data=mdf, ax=axs[3], color='black', alpha=0.1,zorder=0)
axs[3].set_title('(all)')
axs[3].set_xlabel('')
axs[3].set_xticks([0, 1], ['Pre', '48 months'])
axs[3].set_yticks(np.arange(4, 10, step=2))
axs[3].set_ylabel('')
axs[3].set_yticks([])
axs[3].spines['left'].set_visible(False)
axs[3].spines['right'].set_visible(False)
# Adjust layout
plt.tight_layout()
plt.savefig(r"F:\Safavi's project\figure_4_3_c.pdf",dpi=300,format="pdf")

# Show the merged boxplots
plt.show()