from math import hypot


def vector_length(a):
    return hypot(a[0][0] - a[1][0], a[0][1] - a[1][1])
