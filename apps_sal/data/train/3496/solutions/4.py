from math import pi
from operator import mul


def area(args):
    try:
        return mul(*args)
    except TypeError:
        return pi * args**2


def sort_by_area(seq):
    return sorted(seq, key=area)
