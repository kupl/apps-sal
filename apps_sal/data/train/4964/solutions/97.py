def is_uppercase(inp):
    for i in inp:
        if i in 'qwertyuiopasdfghjklzxcvbnm':
            return False
    return True
