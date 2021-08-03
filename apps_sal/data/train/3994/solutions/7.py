from fractions import gcd


def nbr_of_laps(x, y):
    lcm = (x * y) / gcd(x, y)
    return int(lcm / x), int(lcm / y)
