from math import ceil


def factors(n):
    sq = [i for i in range(2, ceil(n**(1 / 2)) + 1) if n % i**2 == 0]
    cb = [i for i in range(2, ceil(n**(1 / 3)) + 1) if n % i**3 == 0]
    return [sq, cb]
