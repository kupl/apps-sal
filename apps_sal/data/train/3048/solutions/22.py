def alternateCase(s):
    return ''.join([x.lower() if x == x.upper() else x.upper() for x in list(s)])
