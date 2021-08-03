def char_freq(message):
    char_list = list(message)
    keys = set(char_list)
    map = {}
    for key in keys:
        map[key] = char_list.count(key)

    return map
