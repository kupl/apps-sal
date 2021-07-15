def super_size(n):
    l = []
    s = ''
    for i in str(n):
        l.append(int(i))
    for i in sorted(l,reverse=True):
        s += str(i)
    return int(s)
