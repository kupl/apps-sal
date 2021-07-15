def string_hash(s):
    t = tuple(map(ord, s))
    a, b = sum(t), sum(y - x for x, y in zip(t, t[1:]))
    return (a | b) & (~a << 2) ^ 32 * (s.count(' ') + 1)
