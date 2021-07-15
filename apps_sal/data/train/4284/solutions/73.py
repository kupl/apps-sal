def array_leaders(n):
    return list(x for i, x in enumerate(n) if x > sum(n[i+1:]))
