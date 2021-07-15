def char_freq(message):
    dict = {}
    for x in message:
        if x not in list(dict.keys()):
            dict[x] = 1
        else:
            dict[x] += 1
    return(dict)

