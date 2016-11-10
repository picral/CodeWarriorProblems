# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:08:33 2016

@author: hg

persistent bugger

https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

"""

def persistence(n):
    n = list(str(n))
        
    count = 0
    while len(n) != 1:
        big_pi = 1
        for i in n:
            big_pi *= int(i)
        n = list(str(big_pi))
        count +=1
    return count
    
    
    
print(persistence(5))