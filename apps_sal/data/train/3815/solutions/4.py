def coprimes(n):
    p, s = n, list(range(n))
    for d in range(2, int(n ** .5) + 1):
        if not p % d:
            while not p % d: p //= d
            s[d::d] = ((n - d - 1) // d + 1) * [0]
    if p > 1: s[p::p] = ((n - p - 1) // p + 1) * [0]
    return [i for i, n in enumerate(s) if n]
