def xor(a, b):
    if not a:
        if b:
            return True
        else:
            return False
    elif not b:
        if a:
            return True
        else:
            return False
    else:
        return False
