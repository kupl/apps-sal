def xor(a,b):
    if a is True:
        if b is True:
            return False
    if a is False:
        if b is False:
            return False
    if b is True:
        if a is True:
            return False
    if b is False:
        if a is False:
            return False
    if a is True:
        if b is False:
            return True
    if b is True:
        if a is False:
            return True
