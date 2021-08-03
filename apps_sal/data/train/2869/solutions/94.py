def distinct(a):
    b = {}
    return [b.setdefault(d, d) for d in a if d not in b]
