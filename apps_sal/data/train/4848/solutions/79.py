def char_freq(message):
    msgL = list(message)
    msgD = dict.fromkeys(msgL)
    for i in msgL:
        if msgD[i] is None:
            msgD[i] = 0
        msgD[i] +=1
    return msgD
