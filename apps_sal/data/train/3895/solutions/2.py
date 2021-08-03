def shifted_diff(first, second):
    return next(iter(i for i in range(len(first)) if first[-i:] + first[:-i] == second), -1)
