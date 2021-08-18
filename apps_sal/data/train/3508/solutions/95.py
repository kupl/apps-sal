import math


def halving_sum(n):
    number = n

    while number >= 1:
        n += (math.floor(number / 2))
        number /= 2

    return n
