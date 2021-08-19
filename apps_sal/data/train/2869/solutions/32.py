def distinct(seq):
    oplst = []
    for s in seq:
        if s not in oplst:
            oplst.append(s)
    return oplst
