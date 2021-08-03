def rotate_clockwise(mx):
    if not mx or not mx[0]:
        return []
    l0, lm, m, r = len(mx[0]), len(mx), [], ''
    while l0:
        lm -= 1
        r += mx[lm][l0 - 1]
        if not lm:
            m.insert(0, r)
            lm = len(mx)
            l0 -= 1
            r = ''
    return m
