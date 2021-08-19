def char_freq(message):
    dict = {}
    characters = []
    for letter in message:
        if letter not in characters:
            characters.append(letter)
            dict[letter] = message.count(letter)
    return dict
