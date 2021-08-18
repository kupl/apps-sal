def array_madness(a, b):
    q = 0
    w = 0
    for i in a:
        q += i**2
    for i in b:
        w += i**3
    return q > w
