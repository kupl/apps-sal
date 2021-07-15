def caeser(message, key):
    return ''.join(chr(65 + (ord(c.upper()) + key - 65) % 26) if c.isalpha() else c for c in message)
