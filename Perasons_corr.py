# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:19:30 2020

@author: dubek
"""

import pandas as pd
import numpy as np
import ruptures as rpt
import matplotlib.pyplot as plt
from sklearn import preprocessing
import seaborn as sns


df = (pd.read_pickle("master_df.pkl")).iloc[:,1:]
df = df.drop(df.columns[5], axis=1)
#df = df.drop('Day-ahead Total Load Forecast [MW] - Greece (GR)')
df = df.rename(columns={"Fossil Brown coal/Lignite  - Actual Aggregated [MW]": "Coal",
                        'Wind Onshore  - Actual Aggregated [MW]':"Wind",
                        'Fossil Gas  - Actual Aggregated [MW]': "Gas",
                        'Solar  - Actual Aggregated [MW]':"Solar",
                        'Total Generation': 'Total Generation',
                        'Day-ahead Price [EUR/MWh]':'Price',
                        "Actual Total Load [MW] - Greece (GR)": 'Actual Load'})

date_rng = pd.date_range(start='1/1/2018', end='2019-12-31 23:00:00', freq='H')


Pcorr = df.corr(method='pearson')
mask = np.triu(np.ones_like(Pcorr, dtype=np.bool))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.set(font_scale=1)
sns.heatmap(Pcorr, mask=mask, annot=True,cmap=cmap)

plt.xlabel(fontsize = 1) # x-axis label with fontsize 15
plt.ylabel(fontsize = 15) # y-axis label with fontsize 15

plt.show()