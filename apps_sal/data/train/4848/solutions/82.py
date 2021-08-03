def char_freq(message):
    d = {}.fromkeys(set(list(message)), 0)
    for i in message:
        d[i] += 1
    return d
