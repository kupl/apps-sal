def char_freq(n):
    d = {}
    for i in n:
        d[i] = n.count(i)
    return d
