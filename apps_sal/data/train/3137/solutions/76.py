import math


def round_it(n):
    left, right = str(n).split('.')
    if len(left) < len(right):
        return math.ceil(n)
    elif len(left) > len(right):
        return math.floor(n)
    return round(n)
