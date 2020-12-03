#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:43:11 2020

@author: Jonatan Scharff Willners
"""
def f(dx, dy, Lines):
    x, y =0,0
    t=0
    while y < len(Lines):
        t += Lines[y][x%(len(Lines[0])-1)] == '#'
        x+=dx
        y+=dy
    return t

file1 = open('input.txt', 'r') 
L = file1.readlines() 
print f(3,1,L)
print f(3,1,L)*f(1,1,L)*f(5,1,L)*f(7,1,L)*f(1,2,L)
