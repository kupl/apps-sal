def is_uppercase(inp):
    for c in inp:
        if c.isalpha() and c.islower():
            return False
    else:
        return True
