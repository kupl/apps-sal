from fractions import gcd


def nbr_of_laps(x, y):
    z = gcd(x, y)
    return (y // z, x // z)
