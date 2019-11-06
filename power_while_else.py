# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:25:44 2019

@author: Jagannath
"""

L = [1, 2, 4, 8, 16, 32, 64]
x = 5
i = 0
while i < len(L) and L[i]!=2**5:
    i=i+1
else:
    print ('Found in position',i+1,'in the list')