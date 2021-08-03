def pattern(n):
    l = []
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            l.append(str(i))
        l.append('\n')
    st = "".join(l)
    return st[:-1]
