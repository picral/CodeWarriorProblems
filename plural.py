# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:21:00 2016

@author: hg

Plural-rank8
https://www.codewars.com/kata/plural/train/python

"""

def plural(n):
    if n == 1: # single item is only case where plural is not true checks if n ==1
        return False
    else:
        return True
print(plural(0))