#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:47:33 2018

@author: maximkuba
"""

import numpy as np
M = 208
N = 12
array = np.zeros((M,N))

array.size



a = np.array([1, 2, 3])

key = int(input('Enter key:'))
print(key)


def find_nearest(z, A):
    id = (np.abs(A-z)).argmin()
    return A[id]

find_nearest(key,a)



    
