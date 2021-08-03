def distinct(seq):
    k = []
    for i in seq:
        if i not in k:
            k += [i]
    return k
