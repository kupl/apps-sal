def tops(msg):
    if len(msg) < 2:
        return ''
    g = 2
    k = ''
    ni = 0
    k += msg[1]
    for i in msg[1:]:
        if ni == g * 2 + 1:
            k += i
            g += 2
            ni = 0
        ni += 1
    return k[::-1]
