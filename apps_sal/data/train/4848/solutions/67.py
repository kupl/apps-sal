def char_freq(msg):
    res = {}
    for c in msg:
        try:
            res[c] += 1
        except KeyError:
            res[c] = 1
    return res
