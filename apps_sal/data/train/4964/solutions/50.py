def is_uppercase(inp):
    return not any(True for c in inp if c.isalpha() and not c.isupper())
