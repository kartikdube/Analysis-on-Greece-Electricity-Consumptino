# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 15:36:16 2020

@author: dubek
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_pickle("master_df.pkl")

date_rng = pd.date_range(start='1/1/2018', end='2019-12-31 23:00:00', freq='H')

ig, ax = plt.subplots()

#ax.plot(date_rng, df['Fossil Brown coal/Lignite  - Actual Aggregated [MW]'], color = "b", label = "Fossil Brown coal/Lignite  - Actual Aggregated [MW]")
#ax.plot(date_rng, df['Fossil Gas  - Actual Aggregated [MW]'], color = "b", label = "Fossil Gas  - Actual Aggregated [MW]")
#ax.plot(date_rng, df['Wind Onshore  - Actual Aggregated [MW]'], color = "b", label = "Wind Onshore  - Actual Aggregated [MW]")
ax.plot(date_rng, df['Solar  - Actual Aggregated [MW]'], color = "b", label = "Solar  - Actual Aggregated [MW]")

ax.set_xlabel("Months")
ax.set_ylabel("Energy [MW]")

ax.legend(loc='upper right', shadow=True, fontsize='large')

plt.show()
