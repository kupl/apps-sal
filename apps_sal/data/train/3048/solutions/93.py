def alternateCase(s):
    s = [x.upper() if x.islower() else x.lower() for x in s]
    s = "".join(s)
    return s
