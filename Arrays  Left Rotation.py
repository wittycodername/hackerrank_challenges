# -*- coding: utf-8 -*-
"""
Created on Mon May  6 13:12:20 2019

@author: mynam
"""

"""
Given an array of size N and a number d, rotate the array to the left by d
i.e. shift the array elements to the left by d.
Ex: The array [1, 2, 3, 4, 5] after rotating by 2 gives [3, 4, 5, 1, 2].
"""

n, d = map(int, input().split())
x = list(input().split())

y = []*n

for i in range (0, n):
    z = x[((i+d) % n)]
    y.append(z)


print(*y, sep=" ")