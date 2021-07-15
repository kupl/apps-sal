def is_uppercase(inp):
    for x in inp:
        if x in "abcdefghijklmnopqrstuvwxyz":
            return False
    return True
