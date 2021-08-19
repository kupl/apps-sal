def spacify(string):
    b = ''
    for i in string:
        b += i + ''
        b += ' '
    b = b[:-1]
    return b
