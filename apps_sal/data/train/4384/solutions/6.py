import fractions


def fraction(a, b):
    return sum([int(s) for s in str(fractions.Fraction(a, b)).split('/')])
