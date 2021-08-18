def alternateCase(s):
    res = ''
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'z':
            res = res + s[i].upper()
        elif s[i] >= 'A' and s[i] <= 'Z':
            res = res + s[i].lower()
        else:
            res = res + s[i]
    return res
