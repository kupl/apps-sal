def distinct(seq):
    res = list()
    for item in seq:
        if item not in res:
            res.append(item)
    return res
