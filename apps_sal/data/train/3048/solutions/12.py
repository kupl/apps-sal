def alternateCase(s):
    return ''.join([x.lower() if x.isupper() else ' ' if x == ' ' else x.upper() for x in s])
