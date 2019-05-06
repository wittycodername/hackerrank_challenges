# -*- coding: utf-8 -*-
"""
Created on Mon May  6 07:51:57 2019

@author: mynam
"""

c.append('#')
         
         
c = [0, 0, 1, 0, 0, 1, 0]


         
def jumpingOnClouds(c):
    
def jumpingOnClouds(c):
    clouds = c
    current = 0
    end = n - 1
    jumps = 0
    while current < end:
        if ((current + 2) <= end) and (clouds[current + 2] == 0):
            current += 2
            jumps += 1
        elif clouds[current + 1] == 0:
            current += 1
            jumps += 1
    return(jumps)

