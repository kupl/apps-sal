def button_sequences(red, blue):
    s = ''
    r, b = False, False
    for i in range(len(red)):
        if red[i] == '0':
            r = False
        if blue[i] == '0':
            b = False
        if red[i] == '1' and not r and not b:
            r = True
            s += 'R'
        elif blue[i] == '1' and not r and not b:
            b = True
            s += 'B'
    return s
