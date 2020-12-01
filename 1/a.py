#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:43:11 2020

@author: Jonatan Scharff Willners
"""

import numpy as np

file1 = open('input.txt', 'r') 
Lines = file1.readlines() 

#print Lines
a = []
for l in Lines:
    a.append(int(l))
    
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            if a[i]+a[j]+a[k] == 2020:
                print a[i], a[j], a[k] 