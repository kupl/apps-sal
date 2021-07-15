def alternateCase(s):
    if len(s) < 1:
        return s
    res = ""
    for l in s:
        if l.isupper():
            res += l.lower()
        else:
            res += l.upper()
    return res
