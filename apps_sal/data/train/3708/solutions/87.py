def hex_to_dec(s):
    hexkey = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15,
    }

    out = 0
    for power, char in enumerate(reversed(s.lower())):
        out += hexkey[char] * (16**power)
    return out
