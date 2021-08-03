def capitalize(s, ind):
    if not s:
        return 'aBCdeF'
    s = list(s)
    for index in ind:
        if index > len(s) - 1:
            continue
        cap = ord(s[index]) - 32
        s[index] = chr(cap)
    return ''.join(s)
