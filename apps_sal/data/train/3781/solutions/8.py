#!/usr/bin/env python
from collections import defaultdict
from itertools import islice

def primes():
    yield 2
    D = defaultdict(list)
    i = 3
    while True:
        if i not in D:
            D[i * i].append(i)
            yield i
        else:
            for k in D[i]:
                j = i + k
                while j % 2 == 0: j += k
                D[j].append(k)
            del D[i]
        i += 2


PRIMES = list(islice(primes(), 1000))

def decompose(n):
    r = defaultdict(int)
    for p in PRIMES:
        while n % p == 0: r[p] += 1; n //= p
        if n == 1: break
    return r


def prod_int_partII(n, s):
    r = []
    d = decompose(n)
    ds = [i for i in range(2, n) if n % i == 0]
    total = sum(i for _, i in list(d.items()))
    q = defaultdict(list)
    def aux(m, ci, c, i=0, p=[]):
        if c == 0:
            if m == 1: q[ci].append(p)
            return
        else:
            for j in range(i, len(ds)):
                if m % ds[j] == 0: aux(m // ds[j], ci, c - 1, j, p + [ds[j]])
    for i in range(2, total + 1): aux(n, i, i)
    return [sum(len(i) for i in list(q.values())), len(q[s]), q[s][0] if len(q[s]) == 1 else q[s]]

