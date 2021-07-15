def xor(a,b):
    '''Function evaluates 2 expressions and returns true if only one of them is true'''
    if a is True and b is True:
        return False
    elif a is True or b is True:
        return True
    else:
        return False
    pass
