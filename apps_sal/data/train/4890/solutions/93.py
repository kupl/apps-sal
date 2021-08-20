from functools import reduce
import math


def find_difference(a, b):
    return math.fabs(reduce(lambda x, y: x * y, a) - reduce(lambda p, q: p * q, b))
