import math


def greatest(x, y, n):
    lcm = x * y // math.gcd(x, y)
    return lcm * (n // lcm) if lcm < n else 0


def smallest(x, y, n):
    lcm = x * y // math.gcd(x, y)
    n2 = int(n // lcm) + 1
    return lcm * n2
