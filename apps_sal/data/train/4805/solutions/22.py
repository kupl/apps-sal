def check(seq, elem):
    x = []
    z = []
    for a in seq:
        if a == elem:
            x.append(a)
        elif a != elem:
            pass
    if x == z:
        return False
    else:
        return True
