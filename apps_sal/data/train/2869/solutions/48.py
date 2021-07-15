def distinct(seq):
    r = []
    s = set()
    for n in seq:
        if n not in s:
            s.add(n)
            r.append(n)
    return r
