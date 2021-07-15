def distinct(seq):
    n = []
    for x in seq:
        if x not in n:
            n.append(x)
    return n
