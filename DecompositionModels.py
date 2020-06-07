# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:02:05 2020

@author: dubek
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_pickle("master_df.pkl")
date_rng = pd.date_range(start='1/1/2018', end='2019-12-31 23:00:00', freq='H')

#series  = pd.DataFrame(list(df['Wind Onshore  - Actual Aggregated [MW]']),index=date_rng)
#series  = pd.DataFrame(list(df['Fossil Brown coal/Lignite  - Actual Aggregated [MW]']),index=date_rng)
#series  = pd.DataFrame(list(df['Fossil Gas  - Actual Aggregated [MW]']),index=date_rng)
#series  = pd.DataFrame(list(df['Solar  - Actual Aggregated [MW]']),index=date_rng)
#series  = pd.DataFrame(list(df['Total Generation']),index=date_rng)
series  = pd.DataFrame(list(df['Day-ahead Price [EUR/MWh]']),index=date_rng)

series = series.fillna(1)
series = series.replace(0,1)
result = seasonal_decompose(series, model='multiplicative')
result.plot()
plt.show()