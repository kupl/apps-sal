def circular_limited_sums(max_n, max_fn):
    p = 12345787
    m = max_fn + 1
    v = [[int(f1 == fn) for fn in range(m)] for f1 in range(m)]
    for n in range(max_n - 1):
        v = [[sum(w[:m - fn]) % p for fn in range(m)] for w in v]
    return sum((sum(w[:m - f1]) % p for (f1, w) in enumerate(v))) % p
