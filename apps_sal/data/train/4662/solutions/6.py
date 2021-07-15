from itertools import count

import numpy as np

primes = np.ones(1000000)
primes[:2] = 0
for i in range(2, len(primes)):
    if primes[i]:
        primes[i * i::i] = 0

non_primes = [1, 4, 6, 8, 9, 10, 14, 16, 18]
def gen_non_primes():
    for x in count(non_primes[-1] + 1):
        if primes[x]:
            continue
        s = str(x)
        if '2' in s or '3' in s or '5' in s or '7' in s:
            continue
        non_primes.append(x)
        yield x
        
def solve(n):
    if n < len(non_primes):
        return non_primes[n]
    for i, np in enumerate(gen_non_primes(), len(non_primes)):
        if i == n:
            return np
