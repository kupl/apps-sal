def alternateCase(s):
    a = []
    for i in s:
        if i.isupper():
            a.append(i.lower())
        else:
            a.append(i.upper())
    return ''.join(a)
