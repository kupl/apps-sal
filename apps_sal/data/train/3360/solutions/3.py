from operator import mul
from functools import reduce


def get_chance(n, x, a):
    return round(reduce(mul,((n-i-x)/(n-i) for i in range(a))), 2)
