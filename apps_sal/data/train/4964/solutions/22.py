def is_uppercase(inp):
    is_char = [c for c in inp if (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122)]
    return all([c.isupper() for c in is_char])
