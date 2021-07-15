def encode(string, key, initShift):
    key = tuple(dict.fromkeys(key.lower() + 'abcdefghijklmnopqrstuvwxyz'))
    shift = (initShift - 1) % 26
    res = ''
    for c in string:
        if c in key:
            i = key.index(c)
            c = key[(i + shift + 1) % 26]
            shift = i
        res += c
    return res


def decode(string, key, initShift):
    key = tuple(dict.fromkeys(key.lower() + 'abcdefghijklmnopqrstuvwxyz'))
    shift = (initShift - 1) % 26
    res = ''
    for i, c in enumerate(string):
        if c in key:
            res += key[(key.index(c) - shift - 1) % 26]
            shift = key.index(res[i])
        else:
            res += c
    return res
