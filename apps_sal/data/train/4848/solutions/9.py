def char_freq(message):
    frequencies = {} 
    for char in message: 
        if char in frequencies: 
            frequencies[char] += 1
        else: 
            frequencies[char] = 1
    return frequencies
