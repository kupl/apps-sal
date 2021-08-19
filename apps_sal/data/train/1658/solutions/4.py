from math import factorial, gcd
from fractions import Fraction


def expand(x, digit):
    (n, d) = (1, factorial(0))
    i = 1
    x = Fraction(x).limit_denominator(10000)
    x1 = x.numerator
    x2 = x.denominator
    while True:
        b = factorial(i)
        if len(str(n)) < digit:
            n = pow(x1, i) * d + n * b * pow(x2, i)
            d *= b * pow(x2, i)
            c = gcd(n, d)
            n //= c
            d //= c
        else:
            break
        i += 1
    return [n, d]
