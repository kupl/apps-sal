def trouble(x, t):
    res = []
    for i in x:
        if not res or res[-1] + i != t:
            res.append(i)
    return res
