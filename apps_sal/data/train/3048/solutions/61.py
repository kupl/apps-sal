def alternateCase(s):

    return "".join(c.upper() if c == c.lower() else c.lower() for c in s)
