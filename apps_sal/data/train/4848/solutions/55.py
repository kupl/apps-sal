def char_freq(message):
    l = {}
    for n in message:
        l[n] = message.count(n)
        n.replace(n, '')
    return l
