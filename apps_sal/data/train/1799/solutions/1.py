def queens(p, s):
    cols = 'abcdefghij'

    def rf(elem):
        if elem == 0:
            return s - 1
        else:
            return elem - 1
    _c = cols.index(p[0])
    _r = rf(int(p[1:]))

    def mf(elem):
        if elem == 10:
            return 0
        else:
            return elem

    def solver(c, dc, r, td, bd, rs):
        if c == s and len(rs) == s:
            return rs
        for i in range(0, s):
            if c == dc:
                return solver(c + 1, dc, r, td, bd, rs)
            ntd = c - i + s - 1
            nbd = -(c + i) + s * 2 - 2
            if r[i] or td[ntd] or bd[nbd]:
                continue
            r[i] = True
            td[ntd] = True
            bd[nbd] = True
            next_r = solver(c + 1, dc, r, td, bd, rs + [i * s + c])
            if next_r:
                return next_r
            r[i] = False
            td[ntd] = False
            bd[nbd] = False
        return False
    fr = [False for i in range(0, s)]
    ftd = [False for i in range(0, s * 2 - 1)]
    fbd = [False for i in range(0, s * 2 - 1)]
    fr[_r] = 1
    ftd[_c - _r + s - 1] = 1
    fbd[-(_c + _r) + s * 2 - 2] = 1
    result = solver(0, _c, fr, ftd, fbd, [_c + _r * s])
    result = ','.join([cols[i % s] + str(mf(i // s + 1)) for i in result])
    return result
