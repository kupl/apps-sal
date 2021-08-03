from fractions import gcd


def are_coprime(n, m):
    return True if gcd(n, m) == 1 else False
