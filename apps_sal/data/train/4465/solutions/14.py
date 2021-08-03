def super_size(n):
    l = [int(i) for i in str(n)]
    s = ""
    while len(l) > 0:
        s += str(l.pop(l.index(max(l))))
    return int(s)
