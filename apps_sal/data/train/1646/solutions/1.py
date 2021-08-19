def green(n):
    vec = [1, 5, 6]
    m1 = 5
    m2 = 6
    tot = 3
    h = 0
    while tot < n:
        s1 = str(m1)
        s2 = str(m2)
        m1 = morph(m1)
        m2 = morph(m2)
        (tot, vec, h) = recover(str(m1), s1, str(m2), s2, vec, tot, h)
    vec.sort()
    return vec[n - 1]


def recover(p, s, r, q, vec, tot, h):
    d = len(p) - len(s)
    d2 = len(r) - len(q)
    for i in range(0, d):
        if p[d - 1 - i] != '0':
            vec.append(int(p[d - 1 - i:d] + s))
            tot += 1
        if r[d2 - 1 - i + h] != '0':
            vec.append(int(r[d2 - 1 - i + h:d2 + h] + q[h:]))
            tot += 1
    return (tot, vec, len(r) - len(p))


def morph(m):
    return (3 * m * m - 2 * m * m * m) % 10 ** (2 * len(str(m)))
