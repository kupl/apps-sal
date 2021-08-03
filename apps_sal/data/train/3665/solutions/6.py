from collections import defaultdict
from bisect import bisect_left


def gen_res(n):
    D = defaultdict(list)
    for q in range(2, n):
        if q not in D:
            D[q * q] = [q]
        else:
            if all(c in allowed for c in str(q)):
                yield q
            for p in D[q]:
                D[p + q].append(p)
            del D[q]


allowed = set("2357")
res = list(gen_res(20000))


def not_primes(a, b):
    return res[bisect_left(res, a):bisect_left(res, b)]
