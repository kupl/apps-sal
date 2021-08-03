def odd(s):
    o = d = res = 0
    for c in filter("od".__contains__, s):
        if c == 'o':
            o += 1
        elif o and d:
            o, d, res = o - 1, d - 1, res + 1
        elif o:
            d += 1
    return res
