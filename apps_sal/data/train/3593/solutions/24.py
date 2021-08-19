def capitalize(s, ind):
    res = ''
    for (i, v) in enumerate(s):
        if i in ind:
            res += v.upper()
        else:
            res += v.lower()
    return res
