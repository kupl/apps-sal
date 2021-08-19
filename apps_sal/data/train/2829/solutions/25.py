def array_madness(a, b):
    aa = sum([i ** 2 for i in a])
    bb = sum([i ** 3 for i in b])
    print(aa, bb)
    return aa > bb
