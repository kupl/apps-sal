def char_freq(message):
    x = {}
    for i in range(len(message)):
        x[message[i]] = message.count(message[i])
    return x
