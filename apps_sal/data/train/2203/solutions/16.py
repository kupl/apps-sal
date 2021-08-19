#!/bin/python3
import sys
n = int(input())
matrix = []
for i in range(n):
    tlist = [int(a) for a in input().split(' ')]
    matrix.append(tlist)

for i in range(n):
    if set(range(n)) == set(matrix[i]):
        big = i
        break

for i in range(n):
    if i == big:
        sys.stdout.write("{} ".format(n))
    else:
        sys.stdout.write("{} ".format(matrix[big][i]))
