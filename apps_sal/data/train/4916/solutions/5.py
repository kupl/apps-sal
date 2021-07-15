def makePrimes(n):
    sieve, primes = [0]*(n+1), []
    for i in range(2, n+1):
        if not sieve[i]:
            primes.append(i) 
            for j in range(i**2, n+1, i): sieve[j] = 1
    return primes

PRIMES = makePrimes(650000)          # => 52831 prime numbers

def get_primes(how_many, group_size=2):

    lst = PRIMES[:how_many] + [None] * (group_size - how_many%group_size)
    
    for n in range(how_many//group_size + bool(how_many%group_size)):
        yield tuple(lst[n*group_size : (n+1)*group_size])
