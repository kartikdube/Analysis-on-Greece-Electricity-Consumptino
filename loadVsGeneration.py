# -*- coding: utf-8 -*-
"""
Created on Sun May 17 02:32:45 2020

@author: dubek
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_pickle("master_df.pkl")

date_rng = pd.date_range(start='1/1/2018', end='2019-12-31 23:00:00', freq='H')

fig, ax = plt.subplots()

ax.plot(date_rng, df['Total Generation'], color = "r", label='Total Generation')
ax.plot(date_rng, df["Actual Total Load [MW] - Greece (GR)"], color = "b", alpha = 0.5, label='Actual Total Load')
ax.set_xlabel("Months")
ax.set_ylabel("Energy [MW]")

legend = ax.legend(loc='upper right', shadow=True, fontsize='large')

plt.show()
