def encode(message, key):
    alphabet_number_pairs = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }
    number_list = []
    alphabet_list = str(key)
    a = 0
    for i in message:
        number_list.append(alphabet_number_pairs[i] + int(alphabet_list[a]))
        a += 1
        if a >= len(alphabet_list):
            a = 0
    return number_list
