BASE = ord('A') - 1


def encode(string):
    return ''.join((str(ord(c) - BASE) if c.isalpha() else c for c in string.upper()))
