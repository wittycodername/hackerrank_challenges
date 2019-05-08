import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    n=len(contests)
    luck = []
    imp = []
    newluck = []
    L = 0

    for i in (1,n):
        lu = [0][i]
        im = [1][i]
        luck.append(lu)
        imp.append(im)

    for i in range (0,n):
        if imp[i] == 0:
            L += luck[i]
            n -= 1
        else:
            newluck.append(luck[i])

    sorted(newluck, reverse='True')
    for i in range (0,n):
        L += newluck[i]
    return(L)
