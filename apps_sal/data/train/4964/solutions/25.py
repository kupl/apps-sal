def is_uppercase(inp):
    for I in inp:
        if ord(I) >= 97 and ord(I) <= 122:
            return False
    return True
