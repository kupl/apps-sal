from fractions import Fraction as F
from math import ceil, floor


def count_black_cells(h, w):
    total = 0
    r = F(h, w)
    last_y = 0
    for x in range(w + 1):
        y = x * r
        total += ceil(y) - floor(last_y)
        if 0 < x < w and y == int(y):
            total += 2
        last_y = y
    return total
