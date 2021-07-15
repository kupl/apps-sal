def char_freq(message):
    r = {}
    for x in message:
        r[x] = r.get(x, 0) + 1
    return r
