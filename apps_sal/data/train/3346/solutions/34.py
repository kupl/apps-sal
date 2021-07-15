import math

def gap(g, m, n):
    primes = []
    gaps = []
    for num in range(m, n+1):
        max_div = math.floor(math.sqrt(num))
        if sum([num % i == 0 for i in range(2,max_div+1)]) == 0:
            primes.append(num)
            diff = primes[primes.index(num)]-primes[primes.index(num)-1]
            if diff == g:
                return [primes[primes.index(num)-1],primes[primes.index(num)]]
