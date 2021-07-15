def char_freq(message):
    dict = {}
    chars = set(message)
    for char in chars:
        dict[char] = message.count(char)
    return dict
