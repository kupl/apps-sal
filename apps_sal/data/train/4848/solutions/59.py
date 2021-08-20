def char_freq(message):
    dictCh = {}
    for ch in message:
        if ch not in dictCh.keys():
            dictCh[ch] = 1
        else:
            dictCh[ch] += 1
    return dictCh
