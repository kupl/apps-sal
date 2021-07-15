from math import *
def sum_cubes(n):
    total = 0
    for i in range(n+1):
        total += int(pow(i,3))
    return total
