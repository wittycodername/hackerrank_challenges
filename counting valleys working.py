# -*- coding: utf-8 -*-
"""
Created on Mon May  6 07:14:15 2019

@author: mynam
"""




s = 'UDDDUDUUDUDUDDUUDDDUUU'


def countingValleys(n, s):

    a = list(s)
    
    height = 0
    valley_count = 0
    
    for i in range(0, n):
        if (a[i]=='U'):
            height += 1
            if (height ==0):
                valley_count +=1
    
        else:
            height -= 1
    return valley_count

    