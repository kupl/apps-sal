def char_freq(message):

    dict = {}

    for char in message:
        dict[char] = 0

    for char in message:
        dict[char] = dict[char] + 1

    return dict
