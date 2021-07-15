def flatten(lst):
    res = []
    for l in lst:
        if isinstance(l, list):
            res.extend(l)
        else:
            res.append(l)
    return res
