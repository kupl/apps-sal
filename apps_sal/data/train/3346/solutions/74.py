from math import sqrt


def isPrime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if(x % i == 0):
            return 0

    return 1


def gap(g, m, n):
    primes = []
    for i in range(m, n + 1):
        if(isPrime(i)):
            primes.append(i)
            if(len(primes) > 1):
                if(primes[-1] - primes[-2] == g):
                    return primes[-2:]

    return None
