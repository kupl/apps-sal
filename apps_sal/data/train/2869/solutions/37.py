def distinct(seq):
    sq = []
    for i in seq:
        if i not in sq:
            sq.append(i)
        else:
            pass
    return sq
