from itertools import accumulate
from bisect import bisect_left
import numpy as np

limit = 555555
sieve = np.ones(limit, dtype=bool)
sieve[0] = sieve[1] = 0
sieve[2*2::2] = 0
for i in range(3, int(len(sieve)**0.5)+1, 2):
    if sieve[i]:
        sieve[i*i::i] = 0
primes = [i for i, x in enumerate(sieve) if x]
acc_primes = list(accumulate([0] + primes))
s_primes = set(primes)


def prime_maxlength_chain(n):
    limit = bisect_left(primes, n)
    ans, max_len = [], 1
    for l in range(limit):
        for r in range(l+max_len, limit+1):
            t = acc_primes[r] - acc_primes[l]
            if t >= n:
                break
            if t in s_primes and r-l >= max_len:
                ans, max_len = ([t], r-l) if r-l > max_len else (ans + [t], max_len)
    return ans
