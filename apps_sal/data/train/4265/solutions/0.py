def tops(msg):
    i,d,s = 1,5, ''
    while i < len(msg):
        s += msg[i]
        i += d
        d += 4
    return s[::-1]
