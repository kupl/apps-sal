def is_uppercase(inp):
    from re import search
    if search(r'[a-z]', inp):
        return False
    return True
