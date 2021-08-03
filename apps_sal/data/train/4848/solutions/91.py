def char_freq(message):
    a = list(dict.fromkeys(message))
    dicts = {}
    for x in a:
        dicts[x] = message.count(x)
    return dicts
