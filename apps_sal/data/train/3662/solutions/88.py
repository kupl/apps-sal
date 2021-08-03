def xor(a, b):
    if a is True and b is True:
        return False
    if a is True and b is False:
        return True
    if a is False and b is True:
        return True
    if a is False and b is False:
        return False
