#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 13:19:44 2018

@author: maximkuba
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




def part2(file):
    lists = pd.read_csv(file)
    print(lists.head(10))
    print(lists['Agency'].head(10))
    print(lists[['Agency', 'Business Title', 'Work Location 1']])


def part3(file):
    lists = pd.read_csv(file)
    lists['Agency'].value_counts(sort=True).plot(kind='bar')
    plt.show()


def part4(file):
    data = pd.read_csv(file)
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


plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)

print(' 2 = part2'
      ' 3 = part3 '
      ' 4 = part4'
      ' 1 = to exit the program')
option = 0
while (option != 1):
    option = int(input('Pick option(1,2,3,4) '))
    if (option == 2):
        part2('NYC_Jobs.csv')
    elif (option == 3):     
        part3('NYC_Jobs.csv')
    elif (option == 4):
        part4('NYC_Jobs.csv')