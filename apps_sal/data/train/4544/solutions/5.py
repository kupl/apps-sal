import math
def factor_sum(n):
    primes = [i for i in range(2, int(math.sqrt(n))+1)]
    while n not in primes:
        if n == sum(prime_factors(n, primes)):
            return n
        n = sum(prime_factors(n, primes))
    return n
    
def prime_factors(n, primes):
    for i in primes:
        for j in primes:
            if j>i and j%i == 0:
                primes.pop(primes.index(j))
    factors = []
    for p in primes:
        while n%p == 0:
            n //= p
            factors.append(p)
    if n != 1:
        factors.append(n)
    return factors
