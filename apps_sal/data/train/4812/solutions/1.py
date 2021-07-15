from math import ceil

def nth_floyd(n):
    return ceil(((8*n + 1) ** 0.5 - 1) / 2)
