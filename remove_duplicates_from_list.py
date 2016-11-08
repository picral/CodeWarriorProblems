# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 23:09:07 2016

@author: hg

remove duplicates from list
https://www.codewars.com/kata/remove-duplicates-from-list/train/python
"""

def distinct(seq):
    arr = []    
    for i in seq:
        if i not in arr:
            arr.append(i)
    return arr