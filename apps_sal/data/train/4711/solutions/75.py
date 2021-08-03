import math


def zeros(n):
    zeroes = 0
    k = 1
    while n / (5**k) > 1:
        zeroes += math.floor(n / (5**k))
        k += 1
    return zeroes
