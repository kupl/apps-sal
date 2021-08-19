def is_uppercase(inp):
    if any((word.islower() for word in inp)):
        return False
    else:
        return True
