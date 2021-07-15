from fractions import Fraction

def sum_fracts(lst):
    if lst:
        ret = sum(Fraction(a, b) for (a, b) in lst)
        return ret.numerator if ret.denominator == 1 else [ret.numerator, ret.denominator]

