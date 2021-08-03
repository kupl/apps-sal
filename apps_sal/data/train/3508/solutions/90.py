import math


def halving_sum(n):
    accum = 0
    while n > 0:
        accum += n
        n = math.floor(n / 2)
    return accum
