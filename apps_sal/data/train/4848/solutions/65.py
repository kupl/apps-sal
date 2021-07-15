def char_freq(message):
    d=dict.fromkeys(message, 0)
    for string in message:
        d[string]+=1
    return d
