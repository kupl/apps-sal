def common(a, b, c):
    d = set(a) & set(b) & set(c)
    a = [i for i in a if i in d]
    b = [i for i in b if i in d]
    c = [i for i in c if i in d]
    return sum([i * min(a.count(i), b.count(i), c.count(i)) for i in d])
