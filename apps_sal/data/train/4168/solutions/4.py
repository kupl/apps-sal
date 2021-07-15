def string_hash(s):
    xs = list(map(ord, s))
    a = sum(xs)
    b = sum(y - x for x, y in zip(xs, xs[1:]))
    c = (a | b) & ((~ a) << 2)
    d = c ^ (32 * (s.count(' ') + 1))
    return d
