def char_freq(message):
    b = {}
    for a in message:
        b.setdefault(a, 0)
        b[a] = b[a] + 1
    return b
