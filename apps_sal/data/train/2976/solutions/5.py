def accum(s):
    return '-'.join([(j * (i + 1)).capitalize() for (i, j) in enumerate(s)])
