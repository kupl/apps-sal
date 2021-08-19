def mix(s1, s2):
    c1 = {l: s1.count(l) for l in s1 if l.islower() and s1.count(l) > 1}
    c2 = {l: s2.count(l) for l in s2 if l.islower() and s2.count(l) > 1}
    r = []
    for c in set(list(c1.keys()) + list(c2.keys())):
        (n1, n2) = (c1.get(c, 0), c2.get(c, 0))
        r.append(('1', c, n1) if n1 > n2 else ('2', c, n2) if n2 > n1 else ('=', c, n1))
    rs = ['{}:{}'.format(i, c * n) for (i, c, n) in r]
    return '/'.join(sorted(rs, key=lambda s: (-len(s), s)))
