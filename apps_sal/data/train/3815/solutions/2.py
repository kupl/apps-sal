from fractions import gcd


def coprimes(n): return [i for i in range(1, n) if gcd(n, i) == 1]
