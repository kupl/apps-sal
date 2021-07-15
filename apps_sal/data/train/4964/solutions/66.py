def is_uppercase(inp):
    r = True
    for c in inp:
        if c.islower():
            r = False
            break
    return r
