# -*- coding: utf-8 -*-
"""
Created on Sun May 24 13:16:43 2020

@author: dubek
"""
import pandas as pd
import numpy as np
import ruptures as rpt
import matplotlib.pyplot as plt
from sklearn import preprocessing
import seaborn as sns


df = pd.read_pickle("master_df.pkl")

date_rng = pd.date_range(start='1/1/2018', end='2019-12-31 23:00:00', freq='H')

mod  = pd.DataFrame(list(df['Wind Onshore  - Actual Aggregated [MW]']), columns = ['Wind Onshore  - Actual Aggregated [MW]'], index=date_rng)
mod['timeStamp'] = date_rng
mod['Months'] = mod['timeStamp'].apply(lambda x: x.strftime('%Y %m/%d'))
mod['Hour'] = mod['timeStamp'].apply(lambda x: x.strftime('%H'))

second_mod =pd.pivot_table(mod, values='Wind Onshore  - Actual Aggregated [MW]', index=['Hour'] , columns=['Months'])

ax = sns.heatmap(second_mod,cmap="YlGnBu")


'''
df["Total Generation"] = df['Fossil Brown coal/Lignite  - Actual Aggregated [MW]'] + 
df['Fossil Gas  - Actual Aggregated [MW]'] + df['Solar  - Actual Aggregated [MW]'] + df['Wind Onshore  - Actual Aggregated [MW]']

ax.set_xticklabels(['2018 Jan','2018 Feb','2018 Mar','2018 Apr','2018 May','2018 Jun','2018 Jul',
                    '2018 Aug','2018 Sep','2018 Oct','2018 Nov','2018 Dec',
                    '2019 Jan','2019 Feb','2019 Mar','2019 Apr','2019 May','2019 Jun','2019 Jul',
                    '2019 Aug','2019 Sep','2019 Oct','2019 Nov','2019 Dec'])
'''
ax.set_title('Wind Onshore  - Actual Aggregated [MW]');