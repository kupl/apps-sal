from fractions import Fraction
from itertools import starmap


def sum_fracts(fractions):
    if not fractions:
        return None

    total = sum(starmap(Fraction, fractions))
    if total.denominator == 1:
        return total.numerator
    return [total.numerator, total.denominator]
