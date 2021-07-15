def array_madness(a,b):
    s = lambda x, y: sum(list(map(lambda z: z ** y, x)))
    return s(a, 2) > s(b, 3)
