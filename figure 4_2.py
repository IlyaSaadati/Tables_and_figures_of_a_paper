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
box_plot=sns.boxplot(x='Exercise intensity 48', y='Excess weight loss 48 (%)', data=df,showcaps=False,palette='GnBu')
sns.stripplot(x='Exercise intensity 48', y='Excess weight loss 48 (%)', data=df, color='black', alpha=0.1,zorder=0)
plt.xlabel('Exercise intensity')
plt.ylabel('Loss of Excess Body Weight (%)')
box_plot.spines['top'].set_visible(False)
box_plot.spines['right'].set_visible(False) 
plt.yticks(np.arange(0, 150, step=50))  # Set label locations.
plt.xticks([0, 1], ['Low', 'Moderate'])
# adding texts to boxes which represent number of data in each box
counts = df['Exercise intensity 48'].value_counts()
plt.text(-0.07, 65, f'N={counts[1]}', fontsize=8)
plt.text(0.9, 140, f'N={counts[2]}', fontsize=8)
plt.savefig(r"F:\Safavi's project\figure_4_2_a.pdf",dpi=300,format="pdf")

plt.show()

#plot 2-2

# creating subdata we need to work on
dfac = df[(df['Exercise intensity 48']==2)]
dflowei = df[df['Exercise intensity 48']==1]

# melting dataframes
mdfac = dfac.melt(value_vars=['BMI Pre (kg/m2)', 'BMI 48 (kg/m2)'])
mdlowei = dflowei.melt(value_vars=['BMI Pre (kg/m2)', 'BMI 48 (kg/m2)'])
mdf = df.melt(value_vars=['BMI Pre (kg/m2)', 'BMI 48 (kg/m2)'])

# main plot
fig, axs = plt.subplots(1, 3, figsize=(10, 5), sharey=False)
# determining  ylim to have same ylim in future subpplots
max_ylim = float(np.max(mdf['value']))+1
min_ylim=float(np.min(mdf['value']))-1
custom_ylim = (min_ylim, max_ylim)
plt.setp(axs,ylim=custom_ylim)


# Create the first boxplot
sns.boxplot(y='value',x='variable',data=mdlowei, ax=axs[0],showcaps=False)
sns.stripplot(y='value',x='variable',data=mdlowei, ax=axs[0], color='black', alpha=0.1,zorder=0)
axs[0].spines['right'].set_visible(False)
# axs[0].set_title('Boxplot 1')
axs[0].title.set_text('Low')
axs[0].set_xlabel('')
axs[0].set_ylabel('BMI (kg/m2)')
axs[0].set_yticks(np.arange(30, 60, step=10))

axs[0].set_xticks([0, 1], ['Pre', '48 months'])


# Create the second boxplot
sns.boxplot(y='value',x='variable',data=mdfac, ax=axs[1],showcaps=False)
sns.stripplot(y='value',x='variable',data=mdfac, ax=axs[1], color='black', alpha=0.1,zorder=0)
axs[1].spines['right'].set_visible(False)
axs[1].spines['left'].set_visible(False)
axs[1].set_title('Moderate')
axs[1].set_xlabel('')
axs[1].set_ylabel('')
axs[1].set_yticks(np.arange(30, 60, step=10))
axs[1].set_yticks([]) # used to make yticks invisible
axs[1].set_xticks([0, 1], ['Pre', '48 months'])

# Create the third boxplot

sns.boxplot(y='value',x='variable',data=mdf, ax=axs[2],showcaps=False)
sns.stripplot(y='value',x='variable',data=mdf, ax=axs[2], color='black', alpha=0.1,zorder=0)
axs[2].set_title('(all)')
axs[2].set_xlabel('')
axs[2].set_xticks([0, 1], ['Pre', '48 months'])
axs[2].set_yticks(np.arange(30, 60, step=10))
axs[2].set_ylabel('')
axs[2].set_yticks([])
axs[2].spines['left'].set_visible(False)
axs[2].spines['right'].set_visible(False)

# Adjust layout
plt.tight_layout()
plt.savefig(r"F:\Safavi's project\figure_4_2_b.pdf",dpi=300,format="pdf")

# Show the merged boxplots
plt.show()


# plot 2-3

# creating subdata we need to work on
dfhac = df[df['Exercise intensity 48']==2]
dfhlow = df[df['Exercise intensity 48']==1]

# melting dataframes
mdfhac = dfhac.melt(value_vars=['HbA1c Pre (mg/dL)', 'HbA1c 48 (mg/dL)'])
mdhlow = dfhlow.melt(value_vars=['HbA1c Pre (mg/dL)', 'HbA1c 48 (mg/dL)'])
mdfh = df.melt(value_vars=['HbA1c Pre (mg/dL)', 'HbA1c 48 (mg/dL)'])

# main plot
fig, axs = plt.subplots(1, 3, figsize=(10, 5), sharey=False)
# determining  ylim to have same ylim in future subpplots
max_ylim = float(np.max(mdfh['value']))+0.5
min_ylim=float(np.min(mdfh['value']))-0.5
custom_ylim = (min_ylim, max_ylim)
plt.setp(axs,ylim=custom_ylim)


# Create the first boxplot
sns.boxplot(y='value',x='variable',data=mdhlow, ax=axs[0],showcaps=False)
sns.stripplot(y='value',x='variable',data=mdhlow, ax=axs[0], color='black', alpha=0.2,zorder=0)
axs[0].spines['right'].set_visible(False)
axs[0].set_title('Boxplot 1')
axs[0].title.set_text('Low')
axs[0].set_xlabel('')
axs[0].set_ylabel('HbA1c (%)')
axs[0].set_yticks(np.arange(4, 12, step=2))

axs[0].set_xticks([0, 1], ['Pre', '48 months'])


# Create the second boxplot
sns.boxplot(y='value',x='variable',data=mdfhac, ax=axs[1],showcaps=False)
sns.stripplot(y='value',x='variable',data=mdfhac, ax=axs[1], color='black', alpha=0.2,zorder=0)
axs[1].spines['right'].set_visible(False)
axs[1].spines['left'].set_visible(False)
axs[1].set_title('Moderate')
axs[1].set_xlabel('')
axs[1].set_ylabel('')
axs[1].set_yticks(np.arange(4, 12, step=2))
axs[1].set_yticks([]) # used to make yticks invisible
axs[1].set_xticks([0, 1], ['Pre', '48 months'])

# Create the third boxplot

sns.boxplot(y='value',x='variable',data=mdfh, ax=axs[2],showcaps=False)
sns.stripplot(y='value',x='variable',data=mdfh, ax=axs[2], color='black', alpha=0.2,zorder=0)
axs[2].set_title('(all)')
axs[2].set_xlabel('')
axs[2].set_xticks([0, 1], ['Pre', '48 months'])
axs[2].set_yticks(np.arange(4, 12, step=2))
axs[2].set_ylabel('')
axs[2].set_yticks([])
axs[2].spines['left'].set_visible(False)
axs[2].spines['right'].set_visible(False)

# Adjust layout
plt.tight_layout()
plt.savefig(r"F:\Safavi's project\figure_4_2_c.pdf",dpi=300,format="pdf")

# Show the merged boxplots
plt.show()


