def rotate_against_clockwise(m, t):
    return rotate_against_clockwise([list(r) for r in zip(*m)][::-1], t % 4 - 1) if t else m
