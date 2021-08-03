def unite_unique(*arg):
    res = []
    for arr in arg:
        for val in arr:
            if not val in res:
                res.append(val)
    return res
