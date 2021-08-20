def encode(s):
    return ''.join((str(ord(c) & 1 ^ 1) if c.isalpha() else c for c in s))
