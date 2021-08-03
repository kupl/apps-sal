def encode(string):
    return ''.join(str(ord(c) - 96) if c.isalpha() else c for c in string.lower())
