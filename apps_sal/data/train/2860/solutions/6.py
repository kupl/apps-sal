def isomorph(a, b):
    return [a.index(h) for h in a] == [b.index(g) for g in b]
