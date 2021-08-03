import math


def find_difference(a, b):
    v1 = a[0] * a[1] * a[2]
    v2 = b[0] * b[1] * b[2]
    return math.abs(v1 - v2)
