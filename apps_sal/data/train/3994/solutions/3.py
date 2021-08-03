from fractions import Fraction


def nbr_of_laps(x, y):
    frac = Fraction(x, y)
    return (frac.denominator, frac.numerator)
