def alternateCase(s=''):
    msg = ''
    if s == '':
        return ''
    for i in s:
        if i.islower():
            msg = msg + str(i.upper())
        elif i.isupper():
            msg = msg + str(i.lower())
        else:
            msg = msg + str(i)
    return msg
