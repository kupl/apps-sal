from math import ceil


def six_column_encryption(msg):
    n = ceil(len(msg) / 6)
    s = (msg + ' ' * (n * 6 - len(msg))).replace(' ', '.')
    r = []
    for i in range(6):
        r.append(s[i::6])
    return ' '.join(r)
