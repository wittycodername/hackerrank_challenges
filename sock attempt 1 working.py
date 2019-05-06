# -*- coding: utf-8 -*-
"""
Created on Mon May  6 07:05:35 2019

@author: mynam
"""

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    ar.append('#')
    import collections
    counter=collections.Counter(ar)
    z = list(counter.values())
    b = len(z)
    pairs = 0
    for i in range (0,b):
        if z[i]  % 2 ==0:
            pairs = pairs + z[i]/2
        else:
            pairs = pairs + (z[i]-1)/2
    return(int(pairs))

sockMerchant(9, 10 20 20 10 10 30 50 10 20)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    
