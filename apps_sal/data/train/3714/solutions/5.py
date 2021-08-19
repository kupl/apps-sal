def encoder(data):
    (d, c, o) = ([''], '', '')
    for i in data:
        (d, c, o) = (d, c + i, o) if c + i in d else (d + [c + i], '', o + str(d.index(c)) + i)
    return o + (str(d.index(c)) if c else '')


def decoder(data):
    (d, c, o) = ([''], '', '')
    for i in data:
        (d, c, o) = (d, c + i, o) if i in '0123456789' else (d + [d[int(c)] + i], '', o + d[int(c)] + i)
    return o + (d[int(c)] if c else '')
