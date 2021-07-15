def alternateCase(s):
    a = s
    b = ''
    for i in range(len(a)):
        if str.isupper(a[i]):
            b += a[i].lower()
        elif a[i] == ' ':
            b += ' '
        else:
            b += a[i].upper()
    return b
