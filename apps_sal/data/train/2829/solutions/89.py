def array_madness(a, b):
    res1 = 0
    for i in a:
        res1 = res1 + i * i

    res2 = 0
    for i in b:
        res2 = res2 + i * i * i

    return res1 >= res2
