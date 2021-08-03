def char_freq(message):
    res = {}
    for v in message:
        if v not in res:
            res[v] = message.count(v)
    return res
