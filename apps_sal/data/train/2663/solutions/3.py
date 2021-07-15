def addsup(a1, a2, a3):
    a3 = set(a3)
    return [[x1, x2, x1 + x2] for x1 in a1 for x2 in a2 if x1 + x2 in a3]
