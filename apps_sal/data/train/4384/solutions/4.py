from fractions import Fraction


def fraction(a, b):
    f = Fraction(a, b)
    return f.numerator + f.denominator
