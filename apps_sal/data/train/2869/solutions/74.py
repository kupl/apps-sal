def distinct(seq):
    l = []
    for i in seq:
        if i not in l:
            l.append(i)
        else:
            pass
    return l
