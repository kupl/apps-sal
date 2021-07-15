def alternateCase(s):
    s = list(s)
    for x in range(len(s)):
        if s[x] == s[x].upper():
            s[x] = s[x].lower()
        else:
            s[x] = s[x].upper()
    return ''.join(s)
