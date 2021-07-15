def xor(a,b):
    if a == True:
        if b == True:
            return False
    if a == True:
        if b == False:
            return True
    if a == False:
        if b == False:
            return False
    if a == False:
        if b == True:
            return True
