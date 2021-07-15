import math
from functools import reduce
#finding primes
MAX_PRIME = 10000
prime_candidates = [True] * MAX_PRIME

for i in range (2,int(math.sqrt(MAX_PRIME)) + 1):
    if prime_candidates[i] == True:
        for j in range(i**2, MAX_PRIME, i):
            prime_candidates[j] = False


def num_primorial(n):
    primes = [i for i,j in enumerate(prime_candidates) if j == True][2:]
    return reduce(lambda x,y : x*y, primes[0:n])
