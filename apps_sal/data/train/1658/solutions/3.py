import math
from fractions import Fraction
from decimal import Decimal


def expand(x, digit):
    x = Fraction(Decimal(x)).limit_denominator(digit)
    incr = 0
    ex = 0
    while len(str(ex.numerator)) < digit:
        ex += Fraction(x ** incr, math.factorial(incr))
        incr = incr + 1
    return [ex.numerator, ex.denominator]
