def alternateCase(s):
    return ''.join(([i.upper(), i.lower()][i.isupper()] for i in s))
