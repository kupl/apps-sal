def xor(a,b):
    if(a == False and b == False):
        return False
    if(a == True and b == True):
        return False
    if(a == False and b == True):
        return True
    if(a == True and b == False):
        return True
