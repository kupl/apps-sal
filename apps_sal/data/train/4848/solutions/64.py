def char_freq(message):
    r = {}
    for m in message: r[m] = r.get(m, 0)+1
    return r
