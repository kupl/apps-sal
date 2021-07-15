def xor(a,b):
    xor = False
    if a == True and b == True:
        xor = False
    elif a == False and b == False:
        xor = False
    elif a == True and b == False:
        xor = True
    elif a == False and b == True:
        xor = True
    return xor
