def hex_to_dec(s):
    h2s = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    dec = 0
    exponent = 0
    for i in range(len(s), 0, -1):
        digit = h2s[s[i - 1].lower()]
        dec = dec + digit * 16 ** exponent
        exponent = exponent + 1
    return dec
