def complete_series(s):
    if len(list(set(s))) == len(s):
        return [d for d in range(max(s) + 1)]
    else:
        return [0]
