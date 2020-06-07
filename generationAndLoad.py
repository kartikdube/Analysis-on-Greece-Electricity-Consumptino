# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 15:31:16 2020

@author: dubek
"""

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

fig, ax = plt.subplots(2)

ax[0].plot(date_rng, df['Total Generation'], color = "r", label='Total Generation')
ax[0].set_title("Total Generation")
ax[1].plot(date_rng, df["Actual Total Load [MW] - Greece (GR)"], color = "b", alpha = 0.5, label='Actual Total Load')
ax[1].set_title("Actual Total Load")
ax[0].set_xlabel("Months")
ax[0].set_ylabel("Energy [MW]")
ax[1].set_xlabel("Months")
ax[1].set_ylabel("Energy [MW]")

plt.show()
