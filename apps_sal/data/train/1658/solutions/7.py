from fractions import Fraction, gcd
from math import floor
def float_to_rat(x):
    def is_int(x):
        return x == floor(x)
    d = 1
    while not is_int(x):
        x *= 10
        d *= 10
    x = int(x);
    g = gcd(x, d)
    return [x // g, d // g]
def expand(x, digit):
    [a, b] = float_to_rat(x)
    x = Fraction(a, b)
    res = Fraction(1)
    new = Fraction(1)
    exponent = 0
    while len(str(res.numerator)) < digit:
        exponent += 1
        new *= x / exponent
        res += new
    return [res.numerator, res.denominator]
