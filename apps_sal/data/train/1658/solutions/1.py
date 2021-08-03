from fractions import Fraction, gcd
from math import floor
from decimal import Decimal


def expand(x, digit):
    x = Fraction(Decimal(str(x)))
    res = Fraction(1)
    new = Fraction(1)
    exponent = 0
    while len(str(res.numerator)) < digit:
        exponent += 1
        new *= x / exponent
        res += new
    return [res.numerator, res.denominator]
