def xor(a, b):
    if a == True and b == True:
        return False
    elif a == True and b == False or (a == False and b == True):
        return True
    else:
        return False
