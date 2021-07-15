LIMIT = 1500000

from math import log, ceil
from itertools import product

m_max, n_max = ceil(log(LIMIT, 2)), ceil(log(LIMIT, 3))
sb_primes = {2}

# generate candidates up to limit
for m, n in product(range(1, m_max), range(n_max)):
    cand = 2**m * 3**n + 1
    # check primality
    if cand < LIMIT and all(cand % x for x in range(3, int(cand**0.5)+1, 2)):
        sb_primes.add(cand)


def solve(x, y):
    return sum(x <= p < y for p in sb_primes)
