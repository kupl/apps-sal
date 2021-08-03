def shuffle_it(a, *b):
    r = a[:]
    for x, y in b:
        r[x], r[y] = r[y], r[x]
    return r
