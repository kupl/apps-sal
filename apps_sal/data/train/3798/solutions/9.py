def cards_and_pero(s):
    c = 0
    d = ''
    rtr = [13, 13, 13, 13]
    l = []
    for i in range(len(s)):
        d = d + s[i]
        c += 1
        if c == 3:
            l.append(d)
            if d in s[i + 1:] or d in s[:i - 1]:
                return [-1, -1, -1, -1]
            d = ''
            c = 0
    print(l)
    while len(l) > 0:
        if l[-1][0] == 'P':
            rtr[0] -= 1
            del l[-1]
        elif l[-1][0] == 'K':
            rtr[1] -= 1
            del l[-1]
        elif l[-1][0] == 'H':
            rtr[2] -= 1
            del l[-1]
        elif l[-1][0] == 'T':
            rtr[3] -= 1
            del l[-1]
    return rtr
