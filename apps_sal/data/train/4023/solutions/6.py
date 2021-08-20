def high(x):
    (s, n) = (x.split(), [sum((ord(c) - 96 for c in y)) for y in x.split()])
    return s[n.index(max(n))]
