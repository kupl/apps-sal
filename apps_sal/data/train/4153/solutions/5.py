cache2, cache, seq = {0: 0}, {0: 0, 1: 0}, {0}


def rec(n):
    if n in cache2:
        return cache[n]
    i = max(cache2)
    r = cache2[i]
    for i in range(i + 1, n):
        cache2[i] = r = [r - i, r + i][(r - i < 0) | (r - i in seq)]
        seq.add(r)
        cache[i + 1] = cache[i] + r
    return cache[n]
