def distinct(seq):
    a = []
    for el in seq:
        if el not in a:
            a.append(el)
    return a
