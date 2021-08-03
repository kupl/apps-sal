def array_madness(a, b):
    sq = 0
    sm = 0
    for i in a:
        sq += i**2
    for i in b:
        sm += i**3

    return sq > sm
