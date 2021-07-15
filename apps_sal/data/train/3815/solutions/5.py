from math import gcd

def coprimes(n):
    return [x for x in range(1, n) if gcd(x, n) == 1]
