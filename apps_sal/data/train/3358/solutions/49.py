def correct(string):
    new = ''
    for i in string:
        if i == '0':
            new = new + 'O'
        elif i == '1':
            new = new + 'I'
        elif i == '5':
            new = new + 'S'
        else:
            new = new + i
    return new
