import math


def sum_cubes(n):
    new = []
    for i in range(1, n + 1):
        x = pow(i, 3)
        new.append(x)
        i = i + 1
    return sum(new)
