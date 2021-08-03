def two_highest(arg1):
    a = []
    a = list(set(arg1))
    a.sort(reverse=True)
    return a[:2] if len(a) > 2 else a
