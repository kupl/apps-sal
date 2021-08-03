from functools import reduce as r
from operator import mul


def find_difference(a, b):
    return abs(r(mul, a, 1) - r(mul, b, 1))
