import math


def goldbach(en):
    r = []
    for j in range(2, int(en / 2) + 1):
        if isPrime(j) and isPrime(en - j):
            r.append([j, en - j])
    return r


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
