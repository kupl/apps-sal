def accum(s):
    a = list(s)
    res = ''
    for (i, c) in enumerate(a):
        res += c * (i + 1) + '-'
    return res.strip('-').title()
