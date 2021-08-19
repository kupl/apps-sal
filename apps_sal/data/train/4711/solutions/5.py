import math


def zeros(n):
    if n >= 5:
        return math.floor(n / 5) + zeros(n / 5)
    else:
        return 0
