def char_freq(message):
    print(message)
    chars = {}
    for char in range(len(message)) :
        if message[char] not in chars :
            chars[message[char]] = 1
        else :
            chars[message[char]] = chars[message[char]] + 1
    return chars
