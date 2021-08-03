def alternateCase(s):
    ret = ''
    for x in s:
        if x == x.upper():
            ret += x.lower()
        else:
            ret += x.upper()
    return ret
