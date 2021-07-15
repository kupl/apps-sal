def distinct(seq):
    i = []
    for x in seq:
        if x not in i:
            i.append(x)
    return i
