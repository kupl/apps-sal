def number(lines):
    res = []
    for (i, v) in enumerate(lines, 1):
        item = '{}: {}'.format(i, v)
        res.append(item)
    return res
