def alternate_sort(l):
    a = sorted([i for i in l if i >= 0])[::-1]
    b = sorted([i for i in l if i not in a])
    res = []
    while len(a) or len(b):
        if len(b):
            res.append(b.pop())
        if len(a):
            res.append(a.pop())
    return res
