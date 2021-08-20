def alternateCase(s):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in s])
