def array_madness(a, b):
    p = 0
    for i in a:
        p += i ** 2
    q = 0
    for j in b:
        q += j ** 3
    return p > q
