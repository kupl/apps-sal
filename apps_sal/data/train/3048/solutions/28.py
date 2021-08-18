def alternateCase(s):
    if s == '':
        return s
    r = ''
    for i in range(len(s)):
        if s[i].islower():
            r += s[i].upper()
        else:
            r += s[i].lower()
    return r
