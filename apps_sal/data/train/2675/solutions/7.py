def bad_apples(a):
    b = list(map(lambda x: [i for i in x if i != 0], a))
    for (x, y) in enumerate(b):
        for (i, j) in enumerate(b):
            if len(y) == 1 and len(j) == 1 and (x != i):
                b[x] = y + j
                b.remove(j)
                break
    return [x for x in b if len(x) == 2]
