def find_dup(l):
    return [v for (i, v) in enumerate(l) if l.index(v) != i][0]
