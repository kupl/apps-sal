def char_freq(message):
    count = {}
    for n in message:
        if (count.get(n)) != None:
            count[n] = count[n] + 1
        else:
            count[n] = 1    
    return count
