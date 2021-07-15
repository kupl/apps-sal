def logical_calc(array, op):
    print(array, op)
    if(op == "AND"):
        if(array.count(False)):
            return False
    elif(op == "OR"):
        if(array.count(True) == 0):
            return False
    else:
        if(array.count(True) % 2 == 0):
            return False
    return True
