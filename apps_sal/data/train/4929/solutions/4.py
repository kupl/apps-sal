def get_diagonale_code(s):
    out, m = [], s.splitlines()
    d, i, j = -1, 0, 0
    while i < len(m) and j < len(m[i]):
        out.append(m[i][j])
        j += 2
        if i in (0, len(m) - 1):
            d = -d
        i += d
    return ''.join(out)
