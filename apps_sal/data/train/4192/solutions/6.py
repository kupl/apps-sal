from collections import defaultdict


def pairwise(arr, n):
    ixs = defaultdict(list)
    for i, e in enumerate(arr):
        ixs[e].append(i)
    h = n / 2
    t = sum(x + y for a, ai in (p for p in ixs.items() if p[0] < h) for x, y in zip(ai, ixs.get(n - a, [])))
    if n % 2:
        return t
    hi = ixs.get(int(h), [])
    return t + sum(hi[:len(hi) // 2 * 2])
