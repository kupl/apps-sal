def send(s):
    r = ''
    state = 0
    for a in (ord(x) for x in s):
        i = 64
        while i > 0:
            b = a & i
            if (state == 0 or state == 2) and b == 0:
                r = r + ' 00 0'
                state = 1
            elif (state == 0 or state == 1) and b != 0:
                r = r + ' 0 0'
                state = 2
            elif state == 2 and b != 0 or (state == 1 and b == 0):
                r = r + '0'
            i = i >> 1
    return r[1:]


def receive(s):
    r = 0
    i = 0
    state = -1
    u = ''
    for c in s:
        if state == -1:
            if c == '0':
                state = 0
        elif state == 0:
            if c == '0':
                state = 1
            else:
                state = 2
        elif state == 1:
            if c == ' ':
                state = 3
        elif state == 2:
            if c == ' ':
                state = -1
            elif c == '0':
                r = r << 1
                r = r + 1
                i = i + 1
        elif state == 3:
            if c == ' ':
                state = -1
            elif c == '0':
                r = r << 1
                i = i + 1
        if i == 7:
            u = u + chr(r)
            i = 0
            r = 0
    return u
