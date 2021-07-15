def func_or(a,b):
    return False if not a and not b else True

def func_xor(a,b):
    return True if (not a and b) or (a and not b) else False
