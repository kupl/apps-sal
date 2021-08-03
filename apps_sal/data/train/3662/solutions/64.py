def xor(a, b):
    if a == False and b == False:
        return False
    elif a == True and b == True:
        return not a
    return a or b
