def capitalize(s):
    (alt, out) = ([0, 1], [list(s), list(s)])
    for i in alt:
        for j in range(len(s)):
            if j % 2 == i:
                out[i][j] = out[i][j].upper()
    return [''.join([x for x in y]) for y in out]
