def prod_int_partII(n, s):
    comb = set()
    for p in partition(n):
        if len(p) > 1:
            comb.add(tuple(sorted(p)))
    res = sorted([p for p in comb if len(p) == s])
    return [len(comb), len(res), list(res[0]) if len(res) == 1 else [list(t) for t in res]]


def partition(n, start=2):
    if n == 1:
        yield []
    for i in range(start, n + 1):
        if n % i == 0:
            for p in partition(n // i, i):
                yield (p + [i])
