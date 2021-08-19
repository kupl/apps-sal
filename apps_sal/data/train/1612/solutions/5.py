from functools import reduce
from operator import mul, gt, lt
from itertools import combinations
from collections import Counter


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


memo = {}


def _prot_part(arr):
    if len(arr) < 2:
        return set({(arr[0],)})
    elif len(arr) == 2:
        return set([tuple(sorted(arr)), (arr[0] * arr[1],)])
    elif tuple(arr) in memo:
        return memo[tuple(arr)]
    r = set()
    for j in range(1, len(arr) // 2 + 1):
        for t in combinations(arr, j):
            arr2 = arr[:]
            for e in t:
                arr2.remove(e)
            s2 = _prot_part(arr2)
            for e1 in _prot_part(list(t)):
                for e2 in s2:
                    r.add(tuple(sorted(list(e1 + e2))))
    r.add((reduce(mul, arr),))
    memo[tuple(arr)] = r
    return r


def find_spec_prod_part(n, com):
    if is_prime(n):
        return 'It is a prime number'
    r = []
    while n % 2 == 0:
        r.append(2)
        n //= 2
    x = 3
    while n > 1 and (not is_prime(n)):
        while n % x == 0:
            r.append(x)
            n //= x
        x += 2
    if n > 1:
        r.append(n)
    p = _prot_part(r)
    if com == 'max':
        m = [None, -1]
        f = gt
    else:
        m = [None, 100000000000.0]
        f = lt
    for t in p:
        if len(t) == 1:
            continue
        (a, b) = (0, 0)
        for (k, v) in Counter(t).items():
            a += k ** v
            b += v
        score = a * b
        if f(score, m[1]):
            m = [sorted(t, reverse=True), score]
    return m
