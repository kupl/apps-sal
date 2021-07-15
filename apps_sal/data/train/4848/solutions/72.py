def char_freq(message):
    dict = {};
    for x in message:
        if not(x in dict):
            dict[x] = 1 
        else:
            dict[x] += 1
    return dict


