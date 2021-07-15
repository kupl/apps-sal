def char_freq(m):
    s = list(m)
    k = set(s)
    v = list(map(lambda x: s.count(x), k))
    return dict(zip(k, v))
