def isomorph(a, b):
    normalize = lambda s: [s.index(c) for c in s]
    return normalize(a) == normalize(b)
