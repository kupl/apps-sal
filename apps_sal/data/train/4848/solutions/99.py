def char_freq(message):
    dct = {}
    for char in message:
        dct[char] = dct.get(char, 0) + 1
    return dct
