def super_size(n):
    s = ''
    a = sorted(str(n))[::-1]
    print(a)
    for j in a:
        s += str(j)
    return int(s)
