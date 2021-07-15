def char_freq(message):
    dct = {}
    for key in message:
        dct[key] = message.count(key)
    return dct
