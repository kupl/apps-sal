from math import gcd, ceil


def rounding(n, m):
    return round(n / m) * m if n != ((n // m) * m + ceil(n / m) * m) / 2 else n
