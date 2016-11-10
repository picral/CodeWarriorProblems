# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 23:27:04 2016

@author: hg

Maximum Subarray Sum

https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python

"""

def maxSequence(arr):
    highest = 0    
    if arr == []:
        return 0
    elif all(i<= 0 for i in arr):
        return 1
    for i in range(len(arr)+1):
        for j in range(len(arr)+1):
            if i < j:
                seriessum = sum(arr[i:j])
                highest = max(seriessum, highest)
    return highest