def char_freq(message):
    words = dict()
    for i in message:
        words[i] = words.get(i,0)+1
    return words
    pass
