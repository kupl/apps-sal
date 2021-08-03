from functools import reduce
from operator import mul


def multi(l_st):
    return reduce(mul, l_st)


def add(l_st):
    return sum(l_st)


def reverse(s):
    return s[::-1]
