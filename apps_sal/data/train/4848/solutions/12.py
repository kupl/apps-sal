def char_freq(message):
    pass
    text = list(message)
    dic = {}
    for x in message:
        dic[x] = text.count(x)
    return dic
