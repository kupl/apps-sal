def ranks(a):
    rankarr = [None] + sorted(a)[::-1]
    return [rankarr.index(x) for x in a]
