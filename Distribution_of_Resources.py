# -*- coding: utf-8 -*-
"""
Created on Thu May 28 01:59:25 2020

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

df = df.drop(['MTU','Total Generation','Actual Total Load [MW] - Greece (GR)','Day-ahead Total Load Forecast [MW] - Greece (GR)',
              'Day-ahead Price [EUR/MWh]'], axis=1)

df.plot.area()
