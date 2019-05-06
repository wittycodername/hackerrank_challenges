# -*- coding: utf-8 -*-
"""
Created on Mon May  6 12:46:20 2019

@author: mynam
"""

grid = list()

for i in range(6):
    row = input().strip().split(' ')
    row = list(map(int, row))
    grid.append(row)


# start max_hourglass_sum at smallest possible hourglass
hourglass_values = []
for i in range(1,5):
    for j in range(1, 5):
            hourglass = grid[i-1][j-1] + grid[i-1][j] +grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1] + grid[i+1][j] +grid[i+1][j+1]
            hourglass_values.append(hourglass)
print(max(hourglass_values))
        