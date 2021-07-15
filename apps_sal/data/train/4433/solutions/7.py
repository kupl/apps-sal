def logical_calc(array, op):
    result = False
    if len(array) == 1: return array[0]
    
    if op == "AND": result = array[0] and array[1]
    if op == "OR": result = array[0] or array[1]
    if op == "XOR": result = array[0] ^ array[1]
    
    for n in range(2,len(array)):
        if op == "AND":
            result = result and array[n]
        if op == "OR":
            result = result or array[n]
        if op == "XOR":
            result = result ^ array[n]
            
    return result
