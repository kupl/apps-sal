def distinct(seq):
    res = []
    for x in seq:
        if res.count(x) == 0:
            res.append(x)
    return res
