def distinct(seq):
    s = set(seq)
    res = []
    for e in seq:
        if e in s:
            res.append(e)
            s.remove(e)
    return res
