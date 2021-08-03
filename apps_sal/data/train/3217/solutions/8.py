from fractions import Fraction
from itertools import starmap


def sum_fracts(lst):
    if lst:
        f = sum(starmap(Fraction, lst))
        return [f.numerator, f.denominator] if f.denominator > 1 else f.numerator
