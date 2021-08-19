def array_madness(a, b):
    hi = 0
    cool = 0
    for num in a:
        p1 = num ** 2
        cool = p1 + cool
    for i in b:
        p2 = i ** 3
        hi = p2 + hi
    if cool > hi:
        return True
    else:
        return False
