def char_freq(message):
    out = {}
    for el in message:
        if el not in out.keys():
            out[el] = 1
        else:
            out[el] += 1
    return out
