def char_freq(message):

    chars = {}
    for char in message:
        try:
            chars[char] = 1 + chars[char]
        except:
            chars[char] = 1

    return chars
