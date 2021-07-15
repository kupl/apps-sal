def rankings(a):
    s = sorted(a)[::-1]
    return [s.index(e) + 1 for e in a]
