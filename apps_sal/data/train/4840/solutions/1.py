def ROTF(U, L, F, R, B, D):
    F = [list(x) for x in zip(*F[::-1])]
    u = list(U[2])
    l = [L[0][2], L[1][2], L[2][2]]
    r = [R[0][0], R[1][0], R[2][0]]
    d = list(D[0])
    U[2] = l[::-1]
    (L[0][2], L[1][2], L[2][2]) = d
    (R[0][0], R[1][0], R[2][0]) = u
    D[0] = r[::-1]
    return (U, L, F, R, B, D)


def ROTS(U, L, F, R, B, D):
    u = list(U[1])
    l = [L[0][1], L[1][1], L[2][1]]
    r = [R[0][1], R[1][1], R[2][1]]
    d = list(D[1])
    U[1] = l[::-1]
    (L[0][1], L[1][1], L[2][1]) = d
    (R[0][1], R[1][1], R[2][1]) = u
    D[1] = r[::-1]
    return (U, L, F, R, B, D)


def perform(a):
    c = 'yyyyyyyyybbbbbbbbbrrrrrrrrrgggggggggooooooooowwwwwwwww'
    (U, L, F, R, B, D) = ([list(c[9 * i:9 * i + 9][j * 3:j * 3 + 3]) for j in range(3)] for i in range(6))
    A = []
    for x in a.replace("'", '3').split():
        if len(x) == 2:
            A += [x[0]] * int(x[1])
        else:
            A += [x]
    TMP = []
    for x in A:
        if x == 'L':
            TMP += list('YYYFY')
        if x == 'l':
            TMP += list('YYYFSY')
        if x == 'R':
            TMP += list('YFYYY')
        if x == 'r':
            TMP += list('YFSYYY')
        if x == 'B':
            TMP += list('YYFYY')
        if x == 'b':
            TMP += list('YYFSYY')
        if x == 'D':
            TMP += list('XFXXX')
        if x == 'd':
            TMP += list('XFSXXX')
        if x == 'U':
            TMP += list('XXXFX')
        if x == 'u':
            TMP += list('XXXFSX')
        if x == 'M':
            TMP += list('YYYSY')
        if x == 'E':
            TMP += list('XSXXX')
        else:
            TMP += [x]
    A = TMP[:]
    for X in A:
        if X == 'F':
            (U, L, F, R, B, D) = ROTF(U, L, F, R, B, D)
        if X == 'S':
            (U, L, F, R, B, D) = ROTS(U, L, F, R, B, D)
        if X == 'f':
            (U, L, F, R, B, D) = ROTF(U, L, F, R, B, D)
            (U, L, F, R, B, D) = ROTS(U, L, F, R, B, D)
        if X == 'Z':
            (U, L, D, R) = (L, D, R, U)
            F = [list(x) for x in zip(*F[::-1])]
            B = [list(x) for x in zip(*B)][::-1]
            U = [list(x) for x in zip(*U[::-1])]
            L = [list(x) for x in zip(*L[::-1])]
            R = [list(x) for x in zip(*R[::-1])]
            D = [list(x) for x in zip(*D[::-1])]
        if X == 'X':
            (U, F, D, B) = (F, D, B, U)
            L = [list(x) for x in zip(*L)][::-1]
            R = [list(x) for x in zip(*R[::-1])]
            B = [list(x) for x in zip(*B)][::-1]
            B = [list(x) for x in zip(*B)][::-1]
            D = [list(x) for x in zip(*D)][::-1]
            D = [list(x) for x in zip(*D)][::-1]
        if X == 'Y':
            (L, F, R, B) = (F, R, B, L)
            U = [list(x) for x in zip(*U[::-1])]
            D = [list(x) for x in zip(*D)][::-1]
        z = ''.join((''.join((''.join(y) for y in x)) for x in (U, L, F, R, B, D)))
    return z
