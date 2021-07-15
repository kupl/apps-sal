def char_freq(message):
    char_list = [str(a) for a in message]
    return {x: char_list.count(x) for x in (char_list)}
