def invert(lst):
    l = []
    for i in lst:
        if i > 0:
            l.append(-i)
        else:
            l.append(abs(i))
    return l
