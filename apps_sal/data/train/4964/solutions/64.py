def is_uppercase(inp):
    for e in inp:
        if e.isalpha():
            if e.islower():
                return False
    return True
