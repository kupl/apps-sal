def xor(a, b):
    if a == False:
        if b == True:
            return True
        elif b == False:
            return False
    if a == True:
        if b == True:
            return False
        elif b == False:
            return True
