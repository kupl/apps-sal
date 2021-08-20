from functools import reduce


def gcd(a, b):
    return gcd(b, a % b) if b else a


def lcm(a, b):
    return a / gcd(a, b) * b


def parameter(n):
    return (lambda n: lcm(sum(n), reduce(lambda a, b: a * b, n, 1)))([int(e) for e in str(n)])
