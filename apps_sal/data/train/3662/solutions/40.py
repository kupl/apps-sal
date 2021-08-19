def xor(a, b):
    if a == False and b == False:
        return False
    if a and b == True:
        return False
    if a or (b == False and a) or b == True:
        return True
