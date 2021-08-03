import math


def zeros(n):
    Zeros = 0
    i = 5
    while i <= n:
        Zeros += math.floor(n / i)
        i *= 5
    return Zeros
