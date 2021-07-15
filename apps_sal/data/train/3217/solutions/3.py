from fractions import Fraction
def sum_fracts(lst):
    if not lst: return None
    r = sum([Fraction(f[0], f[1]) for f in lst])
    return r.numerator if r.denominator == 1 else [r.numerator, r.denominator]
