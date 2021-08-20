def hex_to_dec(s):
    hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    result = 0
    rev = s[::-1]
    for idx in range(len(rev)):
        result += hex[rev[idx]] * 16 ** idx
    return result
