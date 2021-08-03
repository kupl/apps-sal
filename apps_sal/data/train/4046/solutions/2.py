from fractions import Fraction
from functools import reduce
from math import ceil
from operator import mul


def calculate_scrap(scraps, n):
    return ceil(n * 50 * reduce(mul, (Fraction(100, 100 - scrap) for scrap in scraps)))
