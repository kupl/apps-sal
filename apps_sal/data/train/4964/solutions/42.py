def is_uppercase(inp):
    for elem in inp:
        if elem in 'abcdefghijklmnopqrstuvwxyz':
            return False
    return True
