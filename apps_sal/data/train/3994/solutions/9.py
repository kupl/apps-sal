from math import gcd


def nbr_of_laps(x, y):
    g = gcd(x, y)
    return (y // g, x // g)
