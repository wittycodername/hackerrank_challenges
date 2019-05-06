# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:24:33 2019

@author: mynam
"""


# Complete the repeatedString function below.
def repeatedString(s, n):
    string_length = len(s)
    x = s.count('a')
    
    #how many strings?
    a = int(n/string_length)
    #remainder
    b = n % string_length
    
    substring = s[:b]
    y = substring.count('a')
    
    no_of_as = x*a + y
    return(no_of_as)