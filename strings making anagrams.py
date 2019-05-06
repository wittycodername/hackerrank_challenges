# -*- coding: utf-8 -*-
"""
Created on Mon May  6 17:33:56 2019

@author: mynam
"""

from collections import Counter



a = 'fcrxzwscanmligyxyvym'
b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

def removeChars(a, b): 


    intersection = Counter(a) & Counter(b)
    z = list(intersection.elements())
    
    return (len(a)+len(b) - 2 * len(z))


