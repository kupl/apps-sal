def alternateCase(s):
    if len(s) == 0: return s
    res = []
    for x in s:
        if x.isupper(): res.append(x.lower())
        elif x.islower(): res.append(x.upper())
        else: res.append(x)
    return "".join(res)
