def scramble(s, t):
    return (lambda c, d: all((c.get(o, 0) >= d[o] for o in t)))({i: s.count(i) for i in set(s)}, {i: t.count(i) for i in set(t)})
