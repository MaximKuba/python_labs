#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 13:43:34 2018

@author: maximkuba
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)





def task4(name):
    data = pd.read_csv(name)
    data['median'] = data.groupby('Salary Range From')['Salary Range To'].transform(np.median)
    gb = data.groupby('Agency')
    data1 = pd.DataFrame([data.loc[gb.groups[n], 'median'].values for n in gb.groups], index=gb.groups.keys())
    data1 = data1.median(axis=1)
    data1.plot(kind='bar')
    plt.show()

    gb = data.groupby('Work Location')
    data1 = pd.DataFrame([data.loc[gb.groups[n], 'median'].values for n in gb.groups], index=gb.groups.keys())
    data1 = data1.median(axis=1)
    data1[:100].plot(kind='bar')
    plt.show()
task4('NYC_Jobs.csv')