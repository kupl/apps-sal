from math import gcd
from functools import reduce


def solution(a):
    return reduce(gcd, a) * len(a)
