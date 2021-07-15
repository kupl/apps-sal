def complete_series(a):
    return list(range(max(a) + 1)) if len(a) == len(set(a)) else [0]
