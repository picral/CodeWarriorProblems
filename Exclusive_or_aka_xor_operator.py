# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:58:32 2016

@author: hg
Exclusive 'or' (xor) operator

https://www.codewars.com/kata/exclusive-or-xor-logical-operator/train/python
"""

def xor(a,b):
    if (a and not b) or (b and not a):
        return True
    else:
        return False