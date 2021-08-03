import math  # ;-)... (code is only to see what happens for python)
primes, parr = [2, 3, 5, 7], []


def is_prime(n):
    if n < 2:
        return False
    if len(parr) == 0:
        sieve(10000000)
    i, limit = 0, round(math.sqrt(n))
    while True:
        if i >= len(primes):
            primes.append(parr[i])
        if primes[i] > limit:
            break
        if n % primes[i] == 0:
            return False
        i += 1
    return True


def sieve(n):
    array, l = [], int(math.sqrt(n))
    for i in range(n + 1):
        array.append(True)
    for i in range(2, l + 1):
        if array[i]:
            for j in range(i * i, n + 1, i):
                array[j] = False
    for i in range(2, n + 1):
        if array[i]:
            parr.append(i)
