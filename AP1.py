# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:03:50 2020

@author: dubek
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import calmap

ag1 = pd.read_csv('K:\\AA JU DE\\AP1\\Actual Generation per Production Type_201801010000-201901010000.csv')[['MTU','Fossil Brown coal/Lignite  - Actual Aggregated [MW]','Fossil Gas  - Actual Aggregated [MW]','Solar  - Actual Aggregated [MW]','Wind Onshore  - Actual Aggregated [MW]']]
ag2 = pd.read_csv('K:\\AA JU DE\\AP1\\Actual Generation per Production Type_201901010000-202001010000.csv')[['MTU','Fossil Brown coal/Lignite  - Actual Aggregated [MW]','Fossil Gas  - Actual Aggregated [MW]','Solar  - Actual Aggregated [MW]','Wind Onshore  - Actual Aggregated [MW]']]
ag = pd.concat([ag1,ag2], ignore_index = True)

dap1 = pd.read_csv('K:\\AA JU DE\\AP1\\Day-ahead Prices_201801010000-201901010000.csv')
dap2 = pd.read_csv('K:\\AA JU DE\\AP1\\Day-ahead Prices_201901010000-202001010000.csv')
dap = pd.concat([dap1,dap2], ignore_index = True)

tl1 = pd.read_csv('K:\\AA JU DE\\AP1\\Total Load - Day Ahead _ Actual_201801010000-201901010000.csv')
tl2 = pd.read_csv('K:\\AA JU DE\\AP1\\Total Load - Day Ahead _ Actual_201901010000-202001010000.csv')
tl = pd.concat([tl1,tl2], ignore_index = True)

df = (pd.concat([ag,dap,tl], axis = 1)).drop(['MTU (CET)', 'Time (CET)'], axis=1)
df.iloc[1994:1995,1:2],df.iloc[1994:1995,2:3],df.iloc[1994:1995,3:4],df.iloc[1994:1995,4:5],df.iloc[1994:1995,5:6],df.iloc[1994:1995,6:7] , df.iloc[1994:1995,7:8]= 941, 730, 0, 320, 34, 4462, 4438
df.iloc[1996:1998,1:2],df.iloc[1996:1998,2:3],df.iloc[1996:1998,3:4],df.iloc[1996:1998,4:5], df.iloc[1996:1998,7:8]= 945, 700, 0, 201, 4360

df.iloc[10899:10900,1:2],df.iloc[10899:10900,2:3],df.iloc[10899:10900,3:4],df.iloc[10899:10900,4:5],df.iloc[10899:10900,5:6],df.iloc[10899:10900,6:7] , df.iloc[10899:10900,7:8]= 1300, 400, 0, 1302, 56.32, 4474, 4461
df.iloc[1996:1998,1:2],df.iloc[1996:1998,2:3],df.iloc[1996:1998,3:4],df.iloc[1996:1998,4:5], df.iloc[1996:1998,7:8]= 1467, 417, 0, 1200, 4300


df = (df.drop([df.index[7202] , df.index[15934]])).reset_index(drop=True)
df["Total Generation"] = df['Fossil Brown coal/Lignite  - Actual Aggregated [MW]'] + df['Fossil Gas  - Actual Aggregated [MW]'] + df['Solar  - Actual Aggregated [MW]'] + df['Wind Onshore  - Actual Aggregated [MW]']

date_rng = pd.date_range(start='1/1/2018', end='2019-12-31 23:00:00', freq='H')
'''
sambhog  = pd.DataFrame(list(df['Wind Onshore  - Actual Aggregated [MW]']), columns = ['Solar  - Actual Aggregated [MW]'], index=date_rng)
sambhog['timeStamp'] = date_rng
sambhog['Days'] = sambhog['timeStamp'].apply(lambda x: x.strftime('%Y %m/%d'))
sambhog['Hour'] = sambhog['timeStamp'].apply(lambda x: x.strftime('%H'))

second_sambhog =pd.pivot_table(sambhog, values='Solar  - Actual Aggregated [MW]', index=['Hour'] , columns=['Days'])

ax = sns.heatmap(second_sambhog,cmap="YlGnBu")
ax.set(xticklabels=[])
ax.set_title('Wind Onshore  - Actual Aggregated [MW]');


mod  = pd.DataFrame(list(df['Solar  - Actual Aggregated [MW]']), columns = ['Solar  - Actual Aggregated [MW]'], index=date_rng)
mod['timeStamp'] = date_rng
mod['Days'] = mod['timeStamp'].apply(lambda x: x.strftime('%Y %m/%d'))
mod['Hour'] = mod['timeStamp'].apply(lambda x: x.strftime('%H'))

second_mod =pd.pivot_table(mod, values='Solar  - Actual Aggregated [MW]', index=['Hour'] , columns=['Days'])

ax = sns.heatmap(second_mod,cmap="YlGnBu")
ax.set(xticklabels=[])
ax.set_title('Solar  - Actual Aggregated [MW]');

'''
df.to_pickle('master_df.pkl')

#l = list(range(0,17520))
#fig, ax = plt.subplots(2)

#ax[0].plot(l, df["Fossil Brown coal/Lignite  - Actual Aggregated [MW]"])
#plt.show()


