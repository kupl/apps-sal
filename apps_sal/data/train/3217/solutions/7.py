from fractions import Fraction


def sum_fracts(lst):
    f = sum(Fraction(n, d) for n, d in lst)
    return f.numerator or None if f.denominator == 1 else [f.numerator, f.denominator]
