def super_size(n):
    a = [i for i in str(n)]
    out = ''
    while len(a):
        out = out + max(a)
        a.remove(max(a))
    return int(out)
