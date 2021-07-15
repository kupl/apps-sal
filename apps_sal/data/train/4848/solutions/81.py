def char_freq(message):
    set(message)
    character_counts = {}
    for i in set(message):
        count = message.count(i)
        character_counts[i] = count
    return character_counts
    pass
