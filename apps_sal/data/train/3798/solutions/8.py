def cards_and_pero(s):
    c = 0
    d =''
    rtr = [13, 13, 13, 13]
    for i in range(len(s)):
        d = d + s[i]
        c += 1
        if c == 3:
            if d in s[i+1:] or d in s [:i-1]:
                return [-1, -1, -1, -1]
            if d[0] == 'P':
                rtr[0] -= 1
            elif d[0] == 'K':
                rtr[1] -= 1
            elif d[0] == 'H':
                rtr[2] -= 1
            elif d[0] == 'T':
                rtr[3] -= 1
            d = ''
            c = 0
    return rtr     
