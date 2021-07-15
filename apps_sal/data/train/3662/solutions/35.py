def xor(a,b):
    count = 0
    if a == True:
        count += 1
    if b == True:
        count += 1
    if a != True:
        count -= 1
    if b != True:
        count -= 1
    if count == 0:
        return True
    return False
