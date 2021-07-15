def char_freq(message):
    a = {}
    for i in message:
        if i not in a:
            a[i] = 0
        a[i] += 1
    return a
