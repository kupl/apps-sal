def alternateCase(s):
    nw = ''
    for i in s:
        if i.isupper():
            nw += i.lower()
        else:
            nw += i.upper()
    return nw
