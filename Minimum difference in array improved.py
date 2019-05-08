import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    diffs = []
    n = len(arr)
    for i in range (1,n):
                value = abs(arr[i]-arr[i-1])
                diffs.append(value)
    return (min(diffs))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
