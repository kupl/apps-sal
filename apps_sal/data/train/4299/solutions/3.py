from bisect import bisect_left as bisect

PRIMES = [2,3]

def primesBelow(n):
    p = PRIMES[-1]
    while p < n:
        p += 2
        if all(p%x for x in PRIMES): PRIMES.append(p)
    return PRIMES[:bisect(PRIMES,n)]

def is_prime_happy(n):
    return n > 2 and not sum(primesBelow(n)) % n 
