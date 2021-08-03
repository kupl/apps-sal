from fractions import gcd


def nbr_of_laps(x, y):
    return (y / gcd(x, y), x / gcd(x, y))
