from collections import Counter
from functools import reduce
from operator import mul

# The instructions say n<=500_000_000 or 5e8.  However, the tests appear
# to use n<1e12.  We adjust accordingly.

# Use a sieve to pre-compute small primes up to 1e6.  Using trial division
# is sufficent in factoring up to 1e12.  We seed with the first prime to
# simplify is_prime().
small_primes = [2]

# This is suffient for testing primality only up to the square of the
# largest of small_primes.  This is OK to generate the sequence of primes.


def is_prime(n):
    for p in small_primes:
        if p * p > n:
            return True
        if n % p == 0:
            return False


# Sieve to generate the list of small primes.
for n in range(3, 1000000):
    if is_prime(n):
        small_primes.append(n)

# factor an integer up to 1e12


def factor(n):
    if n == 1:
        return Counter()
    for p in small_primes:
        if n % p != 0:
            continue
        factors = factor(n // p)
        factors[p] += 1
        return factors
    return Counter({n: 1})

# count the number of ways of partitioning r objects k ways


def count_partitions(k, r):
    numerator = reduce(mul, list(range(r + 1, r + k)), 1)
    denominator = reduce(mul, list(range(1, k)), 1)
    return numerator // denominator


def multiply(n, k):
    factors = factor(n)
    print(n)
    print(factors)
    return reduce(mul, [count_partitions(k, r) for r in list(factors.values())], 1)
