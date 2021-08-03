def compress(s):
    d = {}
    i = 0
    r = ''
    for w in s.lower().split():
        if w not in d:
            d[w] = i
            i += 1
        r += str(d[w])
    return r
