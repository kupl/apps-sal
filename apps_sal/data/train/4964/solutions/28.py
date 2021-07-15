def is_uppercase(inp):
    for c in inp:
        if c.isalpha() and c == c.lower(): return False
    return True
