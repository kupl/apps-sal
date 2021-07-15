def char_freq(message):
    freqs = {}
    
    index = 0
    while index < len(message):
        if message[index] not in list(freqs.keys()):
            freqs[message[index]] = 1
        else:
            freqs[message[index]] += 1
        index += 1

    return freqs
