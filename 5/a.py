#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:43:11 2020

@author: Jonatan Scharff Willners
"""
import numpy as np

def A(L):
    row = int(L[0:7].replace('F', '0').replace('B', '1'),2)
    seat = int(L[7:10].replace('L', '0').replace('R', '1'),2)
#    print row, seat
    return row*8+seat
def B(L):
    row = int(L[0:7].replace('F', '0').replace('B', '1'),2)
    seat = int(L[7:10].replace('L', '0').replace('R', '1'),2)
#    print row, seat
    return row, seat

file1 = open('input.txt', 'r') 
Lines = [line[:-1] for line in file1]
a = False
if a: print max([A(L) for L in Lines])
#print a
r = 128
s = 8
b = np.zeros((s, r))
for L in Lines:
    tr, ts = B(L)
    b[ts][tr] = 1