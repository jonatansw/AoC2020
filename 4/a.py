#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:43:11 2020

@author: Jonatan Scharff Willners
"""
import re

def list_to_dict(rlist):
    try:
        s = rlist.split(':')
        return {s[0]:s[1]}
    except:
        return {}
#    return dict(map(lambda s : s.split(':'), rlist))

def f(passport):
    sp = passport.split(' ')
    d = {}
    for s in sp:
        d2 = list_to_dict(s)
        d.update(d2)
    
#    for s1 in s:
#d += list_to_dict(s)
#    print"-------"
#    print d
    if 'byr' not in d: return 0
#    print 'byr a'
    if len(d['byr']) != 4: return 0
#    print 'byr b', int(d['byr'])
    if int(d['byr']) <1920 or int(d['byr']) >2002: return 0
#    print 'byr c'
    
    if 'iyr' not in d: return 0
#    print 'iyr a'
    if len(d['iyr']) != 4: return 0
#    print 'iyr b', int(d['iyr'])
    if int(d['iyr']) <2010 or int(d['iyr']) >2020: return 0
#    print 'iyr c'
    
    if 'eyr' not in d: return 0
#    print 'eyr a'
    if len(d['eyr']) != 4: return 0
#    print 'eyr B', int(d['eyr'])
    if int(d['eyr']) < 2020 or int(d['eyr']) > 2030: return 0
#    print 'eyr c'
    
    
    if 'hgt' not in d: return 0
    temp = re.compile("([0-9]+)([a-zA-Z]+)") 
    try:
        res = temp.match(d['hgt']).groups()
    except:
        return 0
    if res[1] == 'in': 
        if int(res[0]) > 76 or int(res[0]) < 59: return 0
    elif res[1] == 'cm':
        if int(res[0]) <150 or int(res[0]) > 193: return 0
    else: return 0
#    print 'hgt'
    
    if 'hcl' not in d: return 0
    if len(d['hcl']) != 7: return 0
    if d['hcl'][0]!='#': return 0
    c_list = ['a', 'b', 'c', 'd', 'e', 'f'] + [str(l) for l in range(10)]
    matched = [c in c_list for c in d['hcl'][1:]]
    if not all(matched): print d['hcl']; return 0
#    print 'hcl'
    
    if 'ecl' not in d: return 0
    if d['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: return 0
    
#    print 'ecl'
    if 'pid' not in d: return 0
#    print 'ecl 2', d['pid']
    if len(d['pid']) != 9: return 0
    if not unicode(d['pid'], 'utf-8').isnumeric(): return 0
#    if 'cid:' not in passport: return 0
#    if 'pid:' not in passport: return 0
#    print "SUCCESS"
    return 1
#    x, y =0,0
#    t=0
#    while y < len(Lines):
#        t += Lines[y][x%(len(Lines[0])-1)] == '#'
#        x+=dx
#        y+=dy
#    return t


file1 = open('input.txt', 'r') 
Lines = [line[:-1] for line in file1]
i=0
valid=0
while i < len(Lines):
    try:
        tempLine = Lines[i]
        i+=1
        passport = ""
        while tempLine != '':
            passport += tempLine + " "
            tempLine = Lines[i]
            i+=1
        valid += f(passport)
#        print passport, f(passport)
    except:
#        break
        valid += f(passport)
#        print passport, f(passport)
print valid
#    print passport
#    print " "