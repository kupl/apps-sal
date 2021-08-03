def super_size(n):
    m = str(n)
    l = list()
    for i in range(len(m)):
        l.append(int(m[i]))
    k = sorted(l, reverse=True)
    res = list()
    for i in range(len(k)):
        res.append(str(k[i]))
    f = ''.join(res)
    return int(f)
