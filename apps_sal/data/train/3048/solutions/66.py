def alternateCase(s):
    return ''.join(c.lower() if str.isupper(c) else c.upper() for c in s)
