def alternateCase(s):
    c = ''
    for i in s:
        if i.isupper():
            c += i.lower()
        elif i.islower():
            c += i.upper()
        else:
            c += ' '
    return c
