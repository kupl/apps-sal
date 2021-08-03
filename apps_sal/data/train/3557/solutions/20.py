import math


def odd_count(n):
    if (n <= 0):
        return 0
    return math.ceil((n - 1) / 2)
