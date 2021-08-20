def chameleon(C, d):
    return (lambda a, b, c: -1 if a == c < 1 or (b - a) % 3 else b)(*sorted([C[i] for i in (0, 1, 2) if i != d]) + [C[d]])
