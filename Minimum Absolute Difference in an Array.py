#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):

    n = len(arr)

    diffs = []
    for i in range (0,n):
        for j in range (0,i):
            if i != j:
                value = abs(arr[i]-arr[j])
                diffs.append(value)

    return(min(diffs))




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
