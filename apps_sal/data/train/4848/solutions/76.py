def char_freq(message):
    result = {}
    for character in message:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    return result
