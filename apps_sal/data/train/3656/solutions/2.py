from fractions import Fraction
from math import ceil


def decompose(n):
    f = Fraction(n)
    result = []
    if f > 1:
        int_part = int(f)
        result = [str(int_part)]
        f -= int_part
    while f:
        x = Fraction(1, ceil(1 / f))
        result.append(str(x))
        f -= x
    return result
