import math


def halving_sum(n):
    half = n / 2
    if half <= 1:
        return math.ceil(half)
    else:
        return math.floor(n + halving_sum(half))
