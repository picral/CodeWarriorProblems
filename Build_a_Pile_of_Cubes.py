# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 23:50:34 2016

@author: hg

Build a pile of cubes

https://www.codewars.com/kata/build-a-pile-of-cubes/train/python
"""

def find_nb(m):
    volume = 0
    i = 0
    while m > 0:
        i += 1
        m -= (i*i*i)
        volume += (i*i*i)
        if m < 0:
            return -1
    return (i)