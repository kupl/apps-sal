def possible_positions(pos):
    col = 'abcdefgh'
    row = '12345678'
    ret = []
    dir = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
    (c, r) = (pos[0], pos[1])
    for d in dir:
        x = col.index(c) + d[0]
        y = row.index(r) + d[1]
        if 0 <= x < 8 and 0 <= y < 8:
            ret.append(''.join([col[x], row[y]]))
    return sorted(ret)
