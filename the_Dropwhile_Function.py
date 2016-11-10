# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 18:04:33 2016

@author: hg

The DropWhile Function

https://www.codewars.com/kata/the-dropwhile-function/train/python
"""

def drop_while(arr, pred):
    arr = iter(arr)
    value = []    
    for x in arr:
        if not pred(x):
            value.append(x)
            break
    for x in arr:
        value.append(x)
    return(value)


is_even=lambda n: not n%2
is_odd=lambda n: n%2

a = [2,6,4,10,1,5,4,3]
b = [2,100,1000,10000,10000,5,3,4,6]

print(drop_while(b,is_even))