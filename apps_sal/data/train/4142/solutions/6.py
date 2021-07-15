def solve(a):
    d = {}
    for i, s in enumerate(a): d.setdefault(frozenset(s), []).append(i)
    return sorted(sum(v) for v in d.values() if len(v) > 1)
