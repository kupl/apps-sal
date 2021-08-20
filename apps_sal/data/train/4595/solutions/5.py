def bishop_diagonal(bishop1, bishop2):

    def coords(p):
        return ('abcdefgh'.index(p[0]), int(p[1]) - 1)

    def pos(i, j):
        return 'abcdefgh'[i] + str(j + 1)
    (x, y) = coords(bishop1)
    (u, v) = coords(bishop2)
    if x + y == u + v:
        d = x + y
        c = [pos(max(0, d - 7), d - max(0, d - 7)), pos(min(7, d), d - min(7, d))]
    elif x - y == u - v:
        d = x - y
        c = [pos(max(0, d), max(0, d) - d), pos(min(7, 7 + d), min(7, 7 + d) - d)]
    else:
        c = [bishop1, bishop2]
    return sorted(c)
