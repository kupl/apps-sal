from fractions import Fraction


def expand(x, digit):
    step = 0
    fact = 1
    expo = Fraction(1)
    n = 10 ** len(str(x).split('.')[-1])
    x = Fraction(int(x * n), n)
    while expo.numerator < 10 ** (digit - 1):
        step += 1
        fact *= step
        expo += x ** step / fact
    return [expo.numerator, expo.denominator]
