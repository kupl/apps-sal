def correct(string):
    c = ''
    for char in string:
        if char == '0':
            c += 'O'
        elif char == '1':
            c += 'I'
        elif char == '5':
            c += 'S'
        else:
            c += char
    return c
