#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:21:53 2018

@author: maximkuba
"""

import xml.etree.ElementTree as ET

parent = ET.Element("data")
child = ET.SubElement(parent, "word")

file = open("a.txt", "r")
words = file.read().split()

word_dictionary = {}
for word in words:
    if word in word_dictionary:
        word_dictionary[word] += 1
    else:
        word_dictionary[word] = 1
file.close()
for word, amount in word_dictionary.items():
    ET.SubElement(child, "name", name=word).text = "amount=" + str(amount)

tree = ET.ElementTree(parent)
tree.write("c1.xml",encoding="utf-8")



            

       