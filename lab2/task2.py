#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 12:52:37 2018

@author: maximkuba
"""
file = open("a.txt", "r")

row = file.readlines()

b1 = open("b1.txt", "w")
b2 = open("b2.txt", "w")
i = 0
for rows in row:
    i += 1
    if i%2 == 0:
        rows = rows.upper()
        b1.write(rows)
    else: 
        rows = rows.lower()
        b2.write(rows)
    
b1.close()
b2.close()
file.close()

b1 = open("b1.txt", "r")
b2 = open("b2.txt", "r")

print("first file")
print(b1.read())
print("second file")
print(b2.read())

b1.close()
b2.close()

        
    

