def encode(msg, k):
    k = ''.join(dict.fromkeys(k)) + ''.join(i for i in 'abcdefghijklmnopqrstuvwxyz' if i not in k)
    r, i = '', 1
    for s in msg:
        x = s.lower()
        if x in k:
            t = k[(k.find(x) + i) % 26]
            r += t.upper() if s.isupper() else t
            i += 1
        else:
            r += s
            i = 1
    return r


def decode(msg, k):
    k = ''.join(dict.fromkeys(k)) + ''.join(i for i in 'abcdefghijklmnopqrstuvwxyz' if i not in k)
    r, i = '', 1
    for s in msg:
        x = s.lower()
        if x in k:
            t = k[(k.find(x) - i) % 26]
            r += t.upper() if s.isupper() else t
            i += 1
        else:
            r += s
            i = 1
    return r
