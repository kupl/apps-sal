def distinct(seq):
    r = []
    for i in seq:
        if not i in r:
            r.append(i)
    return r
