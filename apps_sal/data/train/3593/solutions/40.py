def capitalize(s, ind):
    res = []

    for i, v in enumerate(s):
        if i in ind:
            res.append(v.upper())
        else:
            res.append(v)

    return ''.join(res)
