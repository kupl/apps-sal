def alternateCase(s):
    res = ''
    for c in s:
        if c.isupper():
            res += c.lower()
        else:
            res += c.upper()
    return res
