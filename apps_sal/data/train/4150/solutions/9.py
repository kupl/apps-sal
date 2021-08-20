def rot13(message):
    return ''.join(map(lambda c: chr(ord(c) + 13) if c.isalpha() and c.lower() <= 'm' else chr(ord(c) - 13) if c.isalpha() else c, message))
