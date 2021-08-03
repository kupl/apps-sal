def ranks(a):
    sortA = sorted(a, reverse=True)
    return [sortA.index(s) + 1 for s in a]
