def distinct(seq):
    d = {}
    for s in seq:
        d[s] = 1
    return list(d.keys())
