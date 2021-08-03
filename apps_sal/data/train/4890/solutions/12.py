from functools import reduce
from operator import mul, sub


def find_difference(*cs):
    return abs(sub(*(reduce(mul, c) for c in cs)))
