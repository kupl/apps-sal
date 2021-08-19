def encode(s):
    r = []
    for x in s.split():
        x = x[::-1]
        r.append(x[1:] + x[0])
    return ' '.join(r)
