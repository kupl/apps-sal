def alternateCase(s):
    a = ''
    for x in s:
        if x.islower():
            a += x.upper()
        else:
            a += x.lower()
    return a
