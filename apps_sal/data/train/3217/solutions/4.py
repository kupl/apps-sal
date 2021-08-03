from fractions import Fraction


def sum_fracts(lst):
    out = Fraction(0, 1)
    for x in lst:
        out = out + Fraction(x[0], x[1])
    return None if out.numerator == 0 else out.numerator if out.denominator == 1 else [out.numerator, out.denominator]
