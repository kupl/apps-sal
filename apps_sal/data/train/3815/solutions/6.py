def gcd(a, b):
    while b > 0:
        a %= b
        a, b = b, a
    return a


def coprimes(n):
    return [x for x in range(1, n) if gcd(n, x) == 1]
