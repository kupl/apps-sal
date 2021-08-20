def capitalize(s):
    d = str(s)
    w = ''
    f = ''
    g = []
    for i in range(len(d)):
        if i % 2 == 0:
            w += d[i].upper()
        else:
            w += d[i]
    for i in range(len(d)):
        if i % 2 == 0:
            f += d[i].lower()
        else:
            f += d[i].upper()
    g.append(w)
    g.append(f)
    return g
