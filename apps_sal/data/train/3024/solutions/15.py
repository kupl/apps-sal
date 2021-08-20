def friend(x):
    res = []
    for (i, j) in enumerate(x):
        if len(j) == 4:
            res.append(j)
    return res
