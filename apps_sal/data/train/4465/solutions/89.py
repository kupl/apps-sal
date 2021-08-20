def super_size(n):
    a = []
    b = len(str(n))
    for i in range(b):
        n = str(n)
        a.append(n[i])
    a = sorted(a)
    a = a[::-1]
    c = ''
    for i in range(b):
        c += a[i]
    return int(c)
