def char_freq(message):
    f = {}
    for char in list(message):
        if char in f:
            f[char] += 1
        else:
            f[char] = 1
    return f
