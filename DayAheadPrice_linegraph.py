# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 15:46:03 2020

@author: dubek
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_pickle("master_df.pkl")

date_rng = pd.date_range(start='1/1/2018', end='2019-12-31 23:00:00', freq='H')

fig, ax = plt.subplots()

ax.plot(date_rng, df['Day-ahead Price [EUR/MWh]'], color = "g", label = "Day-ahead Price [EUR/MWh]")

ax.set_xlabel("Months")
ax.set_ylabel("Price [EUR/MWh]")

ax.legend(loc='upper right', shadow=True, fontsize='large')

plt.show()