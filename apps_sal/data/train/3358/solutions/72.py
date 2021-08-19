def correct(string):
    crtd = []
    for x in string:
        if x == '5':
            x = 'S'
        elif x == '0':
            x = 'O'
        elif x == '1':
            x = 'I'
        crtd.append(x)
    return ''.join(crtd)
