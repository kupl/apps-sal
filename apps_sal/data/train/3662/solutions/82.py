def xor(a, b):
    if not a and not b:
        return False
    elif a and not b:
        return True
    elif not a and b:
        return True
    else:
        return False
