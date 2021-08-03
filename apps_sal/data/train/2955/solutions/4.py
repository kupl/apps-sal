def oddest(a):
    b = list(enumerate(a))
    while len(b) > 1:
        b = [(i, v // 2) for i, v in b if v % 2] or [(i, v // 2) for i, v in b]
    return a[b[0][0]]
