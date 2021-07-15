def logical_calc(array, op):
    print((array, op))
    if op == "AND":
        return not (False in array)
    if op == "OR":
        return (True in array)
    status = False
    for bool in array:
        status = bool ^ status  
        
    return status

