def alternateCase(s):
    return ''.join([l.upper() if l.islower() else l.lower() for l in s])
