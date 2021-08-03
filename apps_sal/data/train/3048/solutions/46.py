def alternateCase(s):
    w = ''
    for i in s:
        if i.isupper() == True:
            w += i.lower()
        else:
            w += i.upper()
    return w
