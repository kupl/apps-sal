def digitize(n):
    n = list(str(n))
    l = []
    for i in n:
        a = int(i)
        l.append(a)
    return l[::-1]
