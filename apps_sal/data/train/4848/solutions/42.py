def char_freq(message):
    char = {}
    for i in message:
        if i in char: 
            char[i] += 1
        else: 
            char[i] = 1
        
    return char
