from fractions import Fraction


def calculate_ratio(w, h):
    if w * h == 0:
        raise ValueError()
    return '{0.numerator}:{0.denominator}'.format(Fraction(w, h))
