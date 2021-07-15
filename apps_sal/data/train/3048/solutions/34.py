def alternateCase(s):
    ret = ''
    for c in s:
        if c.isupper():
            ret += c.lower()
        elif c.islower():
            ret += c.upper()
        else:
            ret += c
    return ret
