def char_freq(message):
    dict = {}
    for e in message:
        keys = dict.keys()
        if e in keys:
            dict[e] += 1
        else:
            dict[e] = 1
    return dict
