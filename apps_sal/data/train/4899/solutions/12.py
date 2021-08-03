import math


def weight(n, w):
    i0 = 0.14849853757254047
    return i0 * w * (1 - math.exp(-2 * n)) / (1 - math.exp(-2))
