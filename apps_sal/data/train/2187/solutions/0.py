"""
Codeforces Round 257 Div 1 Problem C

Author  : chaotic_iak
Language: Python 3.3.4
"""

import itertools
from itertools import compress


def read(mode=2):
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


def croft():
    """Yield prime integers using the Croft Spiral sieve.

    This is a variant of wheel factorisation modulo 30.
    """
    for p in (2, 3, 5):
        yield p
    roots = {9: 3, 25: 5}
    primeroots = frozenset((1, 7, 11, 13, 17, 19, 23, 29))
    selectors = (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0)
    for q in compress(
            itertools.islice(itertools.count(7), 0, None, 2),
            itertools.cycle(selectors)
    ):
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
