import math


def halving_sum(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    return math.floor(n) + halving_sum(n / 2)
