# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:19:35 2016

@author: hg

Find Maximum and Minimum Values of a List

https://www.codewars.com/kata/find-maximum-and-minimum-values-of-a-list/train/python

"""

''' requires min and max as function, so cannot use min and max built in functions'''

def min(arr):
    holder = max(arr)
    for i in arr:
        if i < holder:
            holder = i
    return holder    
def max(arr):
    holder = 0    
    for i in arr:
        if i > holder:
            holder = i
    return holder
    
arr = [4,1,3,5,7,9,2]

print(min(arr))