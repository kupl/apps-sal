def simplify(s):
    d, r, c = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}, {(0, 0): ""}, (0, 0)
    for z in s:
        x, y = d[z]
        nc = (c[0] + x, c[1] + y)
        r[nc] = r[nc] if nc in r and r[c].startswith(r[nc]) else r[c] + z
        c = nc
    return r[c]
