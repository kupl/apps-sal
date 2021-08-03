def array_madness(a, b):
    la = sum(x**2 for x in a)
    lb = sum(y**3 for y in b)
    return la >= lb
