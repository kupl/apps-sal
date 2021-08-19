def calc(gamemap):
    (nr, nc) = (len(gamemap), len(gamemap[0]))

    def _i(ra, rb):
        return ra * nr + rb
    (vs, ws) = ([0] * nr ** 2, [0] * nr ** 2)
    for s in range(nr + nc - 1):
        for ra in range(max(0, s - nc + 1), min(s + 1, nr)):
            for rb in range(ra, min(s + 1, nr)):
                ws[_i(ra, rb)] = gamemap[ra][s - ra] + (gamemap[rb][s - rb] if ra != rb else 0) + max((vs[_i(ra - da, rb - db)] for da in (0, 1) if da <= ra for db in (0, 1) if db <= rb))
        (vs, ws) = (ws, vs)
    return vs[-1]
    'SUPER_MAN'
