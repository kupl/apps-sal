def char_freq(m):
    d = dict()
    for i in m:
        d[i] = m.count(i)
    return d
