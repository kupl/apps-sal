def distinct(seq):
    l1 = []
    for x in seq:
        if x not in l1:
            l1.append(x)
    return l1
