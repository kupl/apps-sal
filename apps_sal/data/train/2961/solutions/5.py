def complete_series(s):
    return list(range(max(s) + 1)) if len(set(s)) == len(s) else [0]
