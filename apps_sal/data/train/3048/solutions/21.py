def alternateCase(s):
    alt = ''
    for i in range(len(str(s))):
        if s[i].islower():
            alt += s[i].upper()
        else:
            alt += s[i].lower()
    return alt
