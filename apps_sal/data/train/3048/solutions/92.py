def alternateCase(s):
    return ''.join((l.lower() if l.isupper() else l.upper() for l in s))
