import sys


def hex_to_dec(s):
    hex = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

    res = 0
    weight = 16 ** (len(s) - 1)

    for ch in s:
        if ch in hex:
            res += hex.get(ch) * weight
        else:
            res += int(ch) * weight
        weight /= 16
    return res
