from collections import Counter as C


def solve(n):
    (c, l, li) = (C(str(n)), len(str(n)) - 1, [])
    for i in '75 50 00 25'.split():
        if not C(i) - c:
            (a, b, cn, t) = (i[0], i[1], 0, list(str(n)))
            bi = l - t[::-1].index(b)
            t.insert(l, t.pop(bi))
            ai = l - t[:-1][::-1].index(a) - 1
            t.insert(l - 1, t.pop(ai))
            li.append(l - bi + (l - ai - 1) + [0, next((k for (k, l) in enumerate(t) if l != '0'))][t[0] == '0'])
    return min(li, default=-1)
