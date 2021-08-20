def alternateCase(s):
    res = ''
    for c in s:
        if c.isupper():
            res += c.lower()
        elif c.islower():
            res += c.upper()
        else:
            res += c
    return res
