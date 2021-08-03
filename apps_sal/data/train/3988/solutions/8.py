def encode(string):
    a = ''
    c = 0
    r = ''
    for e in string:
        if e == a:
            c += 1
        else:
            if c > 0:
                r = r + str(c) + a
            a = e
            c = 1
    r = r + str(c) + a
    return r


def decode(string):
    c = 0
    r = ''
    for e in string:
        if e.isdigit():
            c = c * 10 + int(e)
        else:
            r = r + e * c
            c = 0
    return r
