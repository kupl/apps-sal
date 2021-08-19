def capitalize(s):
    o1 = ''
    o2 = ''
    uf = True
    for c in s:
        if uf:
            o1 += c.upper()
            o2 += c
            uf = False
        else:
            o2 += c.upper()
            o1 += c
            uf = True
    return [o1, o2]
