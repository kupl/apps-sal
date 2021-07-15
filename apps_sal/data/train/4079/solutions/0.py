def encode(string):
    return ''.join(str(ord(c.upper())-64) if c.isalpha() else c for c in string)
