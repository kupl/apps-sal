def calc(gamemap):
    (nr, nc) = (len(gamemap), len(gamemap[0]))
    (vs, ws) = ([0] * nr ** 2, [0] * nr ** 2)
    vs[0] = gamemap[0][0]
    for s in range(nr + nc - 2):
        for ra in range(min(s + 1, nr)):
            ca = s - ra
            for rb in range(ra, min(s + 1, nr)):
                cb = s - rb
                v = vs[ra * nr + rb]
                for da in (0, 1):
                    (ra_, ca_) = (ra + da, ca + (1 - da))
                    if ra_ < nr and ca_ < nc:
                        for db in (0, 1):
                            (rb_, cb_) = (rb + db, cb + (1 - db))
                            if rb_ < nr and cb_ < nc:
                                v_ = v + gamemap[ra_][ca_] + (gamemap[rb_][cb_] if ra_ != rb_ else 0)
                                ws[ra_ * nr + rb_] = max(ws[ra_ * nr + rb_], v_)
        (vs, ws) = (ws, vs)
    return vs[-1]
