"""
Codeforces Round 257 Div 1 Problem C

Author  : chaotic_iak
Language: Python 3.3.4
"""

import itertools
from itertools import compress


def read(mode=2):
    # 0: String
    # 1: List of strings
    # 2: List of integers
    inputs = input().strip()
    if mode == 0:
        return inputs
    if mode == 1:
        return inputs.split()
    if mode == 2:
        return [int(x) for x in inputs.split()]


def write(s="\n"):
    if isinstance(s, list):
        s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")

# SOLUTION


# croft algorithm to generate primes
# from pyprimes library, not built-in, just google it


def croft():
    """Yield prime integers using the Croft Spiral sieve.

    This is a variant of wheel factorisation modulo 30.
    """
    # Implementation is based on erat3 from here:
    #   http://stackoverflow.com/q/2211990
    # and this website:
    #   http://www.primesdemystified.com/
    # Memory usage increases roughly linearly with the number of primes seen.
    # dict ``roots`` stores an entry x:p for every prime p.
    for p in (2, 3, 5):
        yield p
    roots = {9: 3, 25: 5}  # Map d**2 -> d.
    primeroots = frozenset((1, 7, 11, 13, 17, 19, 23, 29))
    selectors = (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0)
    for q in compress(
            # Iterate over prime candidates 7, 9, 11, 13, ...
            itertools.islice(itertools.count(7), 0, None, 2),
            # Mask out those that can't possibly be prime.
            itertools.cycle(selectors)
    ):
        # Using dict membership testing instead of pop gives a
        # 5-10% speedup over the first three million primes.
        if q in roots:
            p = roots[q]
            del roots[q]
            x = q + 2 * p
            while x in roots or (x % 30) not in primeroots:
                x += 2 * p
            roots[x] = p
        else:
            roots[q * q] = q
            yield q


n, = read()
cr = croft()
primes = []
for i in cr:
    if i < n:
        primes.append(i)
    else:
        break
primes.reverse()

used = [0] * (n + 1)
res = []
for p in primes:
    k = n // p
    tmp = []
    while k:
        if not used[k * p]:
            tmp.append(k * p)
            used[k * p] = 1
        if len(tmp) == 2:
            res.append(tmp)
            tmp = []
        k -= 1
    if tmp == [p] and p > 2 and p * 2 <= n and len(res) and res[-1][1] == p * 2:
        res[-1][1] = p
        used[p * 2] = 0
        used[p] = 1

print(len(res))
for i in res:
    print(" ".join(map(str, i)))
