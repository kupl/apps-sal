def xor(a, b):
    if a == True:
        if b == True:
            return False
        else:
            return True
    elif b == True:
        if a == True:
            return False
        else:
            return True
    else:
        return False
