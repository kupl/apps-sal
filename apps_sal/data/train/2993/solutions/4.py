def poly_add(p1, p2):
    p = p1[len(p2):] if len(p1) > len(p2) else p2[len(p1):]
    return [i + j for i, j in zip(p1, p2)] + p
