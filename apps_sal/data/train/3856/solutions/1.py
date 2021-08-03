from itertools import compress, takewhile
import numpy as np

s = np.ones(500000)
s[:2] = s[4::2] = 0
for i in range(3, int(len(s)**0.5) + 1, 2):
    if s[i]:
        s[i * i::i] = 0
primes = list(compress(range(len(s)), s))
xs = [primes[i - 1] for i in takewhile(lambda x: x < len(primes), primes)]


def solve(a, b):
    return sum(xs[np.searchsorted(xs, a):np.searchsorted(xs, b, side='right')])
