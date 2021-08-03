def array_madness(a, b):
    a1 = 0
    b1 = 0
    for i in a:
        a1 += i ** 2
    for j in b:
        b1 += j ** 3
    return a1 > b1
