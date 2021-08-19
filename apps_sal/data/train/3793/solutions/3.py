def triangle_type(a, b, c):
    (a, b, c) = sorted([a, b, c])
    if a + b - c <= 0:
        return 0
    (aa_bb, cc) = (a * a + b * b, c * c)
    if aa_bb > cc:
        return 1
    elif aa_bb == cc:
        return 2
    else:
        return 3
