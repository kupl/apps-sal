from fractions import Fraction


def divisible_count(x, y, k):
    x += k - (x % k or k)
    return int(Fraction(y - x + k, k))
