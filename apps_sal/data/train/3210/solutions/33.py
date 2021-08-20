def get_strings(city):
    memory = {}
    for char in city:
        if char.isspace():
            continue
        char = char.lower()
        if char not in memory.keys():
            memory[char] = '*'
        else:
            memory[char] += '*'
    return_str = ''
    for (k, v) in memory.items():
        return_str += k + ':' + v + ','
    return return_str[:-1]
