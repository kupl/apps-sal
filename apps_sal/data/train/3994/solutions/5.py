from fractions import Fraction as frc


def nbr_of_laps(x, y):
    return (frc(x, y).denominator, frc(x, y).numerator)
