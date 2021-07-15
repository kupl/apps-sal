def char_freq(message):
    d = dict()
    chars = list(message)
    for char in chars:
        d[char] = d.get(char,0) + 1
    return d
    

