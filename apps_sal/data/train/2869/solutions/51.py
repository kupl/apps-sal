def distinct(seq):
    l = []
    for elem in seq:
        if elem not in l:
            l.append(elem)
    return l
