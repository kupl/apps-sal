def binary_simulation(s, q):
    (o, l, n) = ([], len(s), int(s, 2))
    for (c, *_) in q:
        if c == 'Q':
            (i,) = _
            o.append(str(n >> l - i & 1))
        else:
            (i, j) = _
            n ^= (1 << l - i + 1) - (1 << l - j)
    return o
