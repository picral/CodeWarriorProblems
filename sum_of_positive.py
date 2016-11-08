# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 22:51:25 2016

@author: hg

sum of positive
https://www.codewars.com/kata/sum-of-positive/train/python
"""

def positive_sum(arr):
    sum = 0
    for i in arr:
        if int(i) > -1:
           sum += i 
    return sum
