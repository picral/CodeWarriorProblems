# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 18:46:24 2016

@author: hg

Linux history and `!` command. Series#1 The `!!` command


"""

def bang_bang(history):
    arr = []
    for i in history.split('\n'):
        arr.append(i.split('  '))
    arr = arr[-1]
    return(arr[-1])