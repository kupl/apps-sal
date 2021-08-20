def chameleon(C, d):
    return (lambda c, a, b: -1 if a == c < 1 or (b - a) % 3 else b)(*[C.pop(d)] + sorted(C))
