def array_madness(a, b):
    newa = []
    newb = []
    for x in a:
        newa.append(x ** 2)
    for y in b:
        newb.append(y ** 3)
    return sum(newa) > sum(newb)
