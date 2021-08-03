def digitize(n):
    n = str(n)
    l = []
    c = list(n)
    c.reverse()
    for i in c:
        l.append(int(i))
    return l
