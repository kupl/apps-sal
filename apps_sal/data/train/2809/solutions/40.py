def digitize(n):
    r = []
    res = str(n)
    for i in res:
        r.append(int(i))
    return r[::-1]
