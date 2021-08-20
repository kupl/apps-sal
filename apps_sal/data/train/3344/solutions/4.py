import math


def number_property(n):
    return [isprime(n), n % 2 == 0, n % 10 == 0]


def isprime(fltx):
    if fltx == 2:
        return True
    if fltx <= 1 or fltx % 2 == 0:
        return False
    return all((fltx % i != 0 for i in range(3, int(math.sqrt(fltx)) + 1, 2)))
