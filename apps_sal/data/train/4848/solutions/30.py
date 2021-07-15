def char_freq(message):
    count = {}
    for character in message:
        count.setdefault(character, 0)
        count[character] += 1
    return count
