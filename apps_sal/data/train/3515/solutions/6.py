def encode(text, key):
    k = ''
    for c in key + 'abcdefghijklmnopqrstuvwxyz':
        if c not in k:
            k += c
    r = ''
    i = 1
    for c in text:
        if c.isalpha():
            j = (k.index(c.lower()) + i) % 26
            if c.isupper():
                r += k[j].upper()
            else:
                r += k[j]
            i += 1
        else:
            r += c
            i = 1
    return r


def decode(text, key):
    k = ''
    for c in key + 'abcdefghijklmnopqrstuvwxyz':
        if c not in k:
            k += c
        r = ''
    i = 1
    for c in text:
        if c.isalpha():
            j = (k.index(c.lower()) - i) % 26
            if c.isupper():
                r += k[j].upper()
            else:
                r += k[j]
            i += 1
        else:
            r += c
            i = 1
    return r
    return text
