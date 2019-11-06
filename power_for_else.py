# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:31:01 2019

@author: Jagannath
"""

L = [1, 2, 4, 8, 16, 32, 64]
x = 2
for i in range(len(L)):
    if L[i]==2**x:
        j=i   # extra variable to store the position where it is found
        i=len(L)+1  # So when it is found the condition in for is made false 
                    #so that control will be directed to else part of for
    else:
        print ('Not found in position',i+1)
else:
    print ('Found in position',j+1,'in the list')