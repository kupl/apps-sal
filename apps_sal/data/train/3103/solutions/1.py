def unique(integers):
    l = []
    for i in integers:
        if not i in l: l.append(i)
    return l
