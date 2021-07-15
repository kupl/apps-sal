def correct(string):
    r = ""
    for c in string:
        if c == '0':
            r += 'O'
        elif c == '1':
            r += 'I'
        elif c == '5':
            r += 'S'
        else:
            r += c
    return r
