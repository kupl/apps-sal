from itertools import combinations, compress
import numpy as np
s = np.ones(100000)
s[:2] = s[2::2] = 0
for i in range(3, int(len(s) ** 0.5) + 1, 2):
    if s[i]:
        s[i * i::i] = 0
primes = list(compress(range(len(s)), s))


def primes_a_p(lower_limit, upper_limit):
    xs = primes[np.searchsorted(primes, lower_limit):np.searchsorted(primes, upper_limit)]
    return [list(range(a, a + 6 * (b - a), b - a)) for (a, b) in combinations(xs, 2) if all((x <= upper_limit and s[x] for x in range(b + b - a, a + 6 * (b - a), b - a)))]
