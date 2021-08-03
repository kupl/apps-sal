from operator import mul
from functools import reduce


def find_difference(a, b):
    return abs(reduce(mul, a) - reduce(mul, b))
