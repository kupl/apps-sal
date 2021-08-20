import math


def area_largest_square(r):
    d = 2 * r
    v = d ** 2
    l = math.sqrt(v)
    a = l * l / 2
    return a
