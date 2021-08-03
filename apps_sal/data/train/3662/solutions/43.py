def xor(a, b):
    if a == True and b == True:
        return False
    elif a == True and b == False:
        return True
    elif b == True and a == False:
        return True
    elif a == False and b == False:
        return False
