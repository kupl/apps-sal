def isprime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True


def gap(g, m, n):
    primes = (i for i in range(m, n + 1) if isprime(i))
    primes2 = (i for i in range(m, n + 1) if isprime(i))
    next(primes2)
    for p1, p2 in zip(primes, primes2):
        if p2 - p1 == g:
            return [p1, p2]
    return None
