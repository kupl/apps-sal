def correct(string):
    a = ''
    for x in string:
        if x == '5':
            a += 'S'
        elif x == '0':
            a += 'O'
        elif x == '1':
            a += 'I'
        else:
            a += x
    return a
