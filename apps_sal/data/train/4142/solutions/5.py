def solve(arr):
    sums = {}
    for i, s in enumerate(arr):
        sums.setdefault(frozenset(s), []).append(i)
    return sorted(sum(indexes) for indexes in sums.values() if len(indexes) > 1)
