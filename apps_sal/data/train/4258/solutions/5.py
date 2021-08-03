from fractions import Fraction


def series_sum(n):
    total = sum(Fraction(1, 1 + i * 3) for i in range(n))
    return '{:.2f}'.format(total.numerator / total.denominator)
