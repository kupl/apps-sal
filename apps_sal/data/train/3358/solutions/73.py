def correct(string):
    new_s = ''
    for i in string:
        if not i.isdigit():
            new_s += i
        elif i == '0':
            new_s += 'O'
        elif i == '5':
            new_s += 'S'
        else:
            new_s += 'I'
    return new_s
