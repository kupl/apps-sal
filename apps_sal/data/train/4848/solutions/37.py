lets = "().!?,-' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRQSTUVWXYZ"
def char_freq(message):
    retDict={}
    for l in lets:
        if message.count(l)>0:
            retDict[l]= message.count(l)
    return retDict
