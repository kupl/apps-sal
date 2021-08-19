def mid_endian(n):
    s = format(n, 'x')
    s = '0' + s if len(s) % 2 else s
    (r, c) = ('', 0)
    while s:
        if not c % 2:
            r += s[:2]
        else:
            r = s[:2] + r
        c += 1
        s = s[2:]
    return r.upper()
