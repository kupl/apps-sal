def is_uppercase(inp):
    a = [c for c in inp if c.islower()]
    return False if a else True
