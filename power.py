# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:16:06 2019
 Searching of 2^x in a list
@author: Jagannath
"""
L = [1, 2, 4, 8, 16, 32, 64]
X = 5
found = False
i = 0
while not found and i < len(L):
    if 2 ** X == L[i]:
        found = True
    else:
        i = i+1
if found:
    print('at index', i)
else:
    print(X, 'not found')
