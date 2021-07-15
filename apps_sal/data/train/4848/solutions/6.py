def char_freq(message):
    chars = {}
    for char in message:
        chars[char] = chars.get(char, 0) + 1
    return chars
