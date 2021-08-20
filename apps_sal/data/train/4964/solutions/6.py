def is_uppercase(inp):
    from re import search
    if search('[a-z]', inp):
        return False
    return True
