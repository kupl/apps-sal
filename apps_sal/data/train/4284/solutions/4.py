def array_leaders(n):
    return [e for (i, e) in enumerate(n, 1) if e > sum(n[i:])]
