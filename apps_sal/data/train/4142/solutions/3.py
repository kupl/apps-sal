from collections import defaultdict

def solve(arr):
    d = defaultdict(list)
    for i, x in enumerate(arr):
        d[frozenset(x)].append(i)
    return sorted(sum(xs) for xs in list(d.values()) if len(xs) > 1)

