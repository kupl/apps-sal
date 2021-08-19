def char_freq(message):
    characters = {}
    for char in message:
        characters[char] = characters.get(char, 0) + 1
    return characters
