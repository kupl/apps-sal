from bisect import bisect
from itertools import product
is_prime = lambda n: n % 2 and all(n % x for x in range(3, int(n ** .5) + 1, 2))
prime_digits = (int(''.join(p)) for k in range(2, 6) for p in product('2357', repeat=k))
non_primes = [n for n in prime_digits if not is_prime(n)]
not_primes = lambda a, b: non_primes[bisect(non_primes, a-1): bisect(non_primes, b-1)]
