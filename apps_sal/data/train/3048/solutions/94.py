def alternateCase(s):
    return ''.join([l.upper() if l.islower() else l.lower() if l.isupper() else l for l in s])
