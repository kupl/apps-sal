def duplicates(arr):
    res = []
    for (i, x) in enumerate(arr):
        if arr[:i + 1].count(x) > 1 and x not in res:
            res.append(x)
    return res
