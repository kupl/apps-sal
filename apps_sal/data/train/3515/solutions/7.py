def encode(text, key):
    return cipher(text, key, 1)


def decode(text, key):
    return cipher(text, key, -1)


def cipher(text, key, mode):
    U = tuple(dict.fromkeys(key.upper() + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    L = tuple(dict.fromkeys(key.lower() + 'abcdefghijklmnopqrstuvwxyz'))
    output = ''
    i = mode
    for x in text:
        if x in U:
            output += U[(U.index(x) + i) % 26]
            i += mode
        elif x in L:
            output += L[(L.index(x) + i) % 26]
            i += mode
        else:
            output += x
            i = mode
    return output
