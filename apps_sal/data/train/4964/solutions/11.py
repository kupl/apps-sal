def is_uppercase(inp):
    for s in inp:
        if s.isalpha() and not s.isupper():
            return False
    return True
