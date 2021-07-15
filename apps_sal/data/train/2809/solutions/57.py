def digitize(n):
    n = str(n)
    l = list()
    n = n[::-1]
    for s in n:
        l.append(int(s))
    return l

