def chameleon(C, d):
    c = C.pop(d)
    a, b = sorted(C)
    return(a == c < 1) + (b - a) % 3 and -1 or b
