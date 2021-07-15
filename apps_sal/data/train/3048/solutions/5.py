def alternateCase(s):
    ret = ""
    for c in s:
        if c.isalpha():
            if c.isupper():
                ret += c.lower()
            else:
                ret += c.upper()
        else:
            ret += c
    return ret
