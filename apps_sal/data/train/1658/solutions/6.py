import fractions as fr
from decimal import Decimal as Dec


def expand(x, digit):
    f = fr.Fraction(Dec(x)).limit_denominator()
    (xn, xd) = (f.numerator, f.denominator)
    (i, n, num, den) = (0, 1, 1, 1)
    while len(str(n)) < digit:
        i += 1
        num = num * i * xd + xn ** i
        den *= i * xd
        f = fr.Fraction(num, den)
        (n, d) = (f.numerator, f.denominator)
    return [n, d]
