def char_freq(message):
    ABC = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = []
    letters = []
    for l in message:
        c = message.count(l)
        if c > 0:
            count.append(c)
            letters.append(l)
    return dict(zip(letters, count))
    pass
