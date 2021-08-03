def encode(s):
    return ''.join(str((ord(c.lower()) - 97) % 2) if c.isalpha() else c for c in s)
