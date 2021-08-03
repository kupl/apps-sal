def char_freq(message):
    char = {}
    for c in message:
        if c in char:
            char[c] += 1
        else:
            char[c] = 1
    return char
