def char_freq(message):
    result = {}
    for letter in message:
        result[letter] = result.get(letter, 0) + 1
    return result
