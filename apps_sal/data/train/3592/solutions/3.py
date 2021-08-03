from fractions import gcd


def greatest(x, y, n):
    lcm = x * y // gcd(x, y)
    return (n - 1) // lcm * lcm


def smallest(x, y, n):
    lcm = x * y // gcd(x, y)
    return -(- (n + 1) // lcm) * lcm
