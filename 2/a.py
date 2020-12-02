#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:43:11 2020

@author: Jonatan Scharff Willners
"""

import numpy as np
import re

def isValid(l):
    mini, maxi, c, s = re.split('-|: | ', l)
    a = int(mini) <= s.count(c) <= int(maxi)
    b = int(s[int(mini)-1] == c) + int(s[int(maxi)-1] == c) == 1
    return a, b

file1 = open('input.txt', 'r') 
Lines = file1.readlines() 

validA = 0
validB = 0
for l in Lines:
    a, b = isValid(l)
    validA+=a
    validB+=b
print validA, " ", validB
