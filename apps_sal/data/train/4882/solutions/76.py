import math


def round_to_next5(n):
    a = n
    nearest_multiple = 5 * math.ceil(a / 5)
    return nearest_multiple
