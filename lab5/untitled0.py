#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 01:29:30 2018

@author: maximkuba
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sympy import *


x = [-4.8,-4.1,-5.3,-4.2,-4.9]
y = [1.108,0.940,1.283,0.954,1.140]
xs = Symbol('x')

def algorithm(x,y,xs):
    Lx = 0
    for j in  range (len(y)):
        value = 0
        for i in range (len(x)):
            if i!=j:
                value = (xs - x[i])/(x[j] - x[i])
        Lx += y[j]* value
    return Lx
algorithm(x,y,xs)
plt.plot(x,y)



