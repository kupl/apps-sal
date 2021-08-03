def invert(lst):
    list = []
    for l in lst:
        if l < 0:
            list.append(abs(l))
        else:
            list.append(-abs(l))
    return list
