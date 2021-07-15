def ranks(a):
    s = sorted(a)[::-1]
    return [(s.index(n) + 1) for n in a]

