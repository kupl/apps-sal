from fractions import gcd

def nbr_of_laps(x, y):
    lcm = x / gcd(x, y) * y
    return lcm/x, lcm/y
