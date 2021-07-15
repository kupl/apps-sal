from bisect import bisect_left

def sieve(n):
    sieve, primes = [0]*(n+1), []
    for i in range(2, n+1):
        if not sieve[i]:
            primes.append(i)
            for j in range(i**2, n+1, i): sieve[j] = 1
    return primes

PRIMES = sieve(100000)

def prime_primes(n):
    lst = PRIMES[:bisect_left(PRIMES, n)]
    divs = [p/q for i,p in enumerate(lst) for q in lst[i+1:]]
    return len(divs), int(sum(divs))
