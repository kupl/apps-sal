from fractions import Fraction


def sum_fracts(lst):
    s = sum(Fraction(*f) for f in lst)
    if s:
        return s.numerator if s.denominator == 1 else [s.numerator, s.denominator]
