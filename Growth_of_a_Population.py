# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 15:53:25 2016

@author: hg

Growth of a Population

https://www.codewars.com/kata/growth-of-a-population/train/python

"""

def nb_year(p0, percent, aug, p):
    percent = percent/ 100
    yearcount = 0    
    while p > p0:
        p0 = (p0 * (1+percent))+ aug
        yearcount += 1
    return yearcount
print(nb_year(1500, 5, 100, 5000))