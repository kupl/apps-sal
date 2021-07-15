def is_uppercase(inp):
    for c in inp:
        if c.isalpha() and ord(c) >= 97:
            return False
    return True
