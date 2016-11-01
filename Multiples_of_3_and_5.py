# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:05:34 2016

@author: hg

multiples of 3 and 5 -rank6
https://www.codewars.com/kata/multiples-of-3-and-5/train/python

"""

def solution(number):
    solset = [] #initializes solution set   
    for i in range(number):
        if i%3 == 0 or i%5 == 0:    #checks if 3 or 5 is a factor and adds to solset
            solset.append(i)
    return sum(solset)#returns sum of solset
print(solution(10))