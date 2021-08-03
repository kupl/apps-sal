def alternateCase(s):
    res = ""
    for c in s:
        res += c.upper() if c.islower() else c.lower()
    return res
