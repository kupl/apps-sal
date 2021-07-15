def logical_calc(array, op):
    if op == 'AND': return False not in array
    if op == 'OR': return True in array
    
    result = array[0]
    
    for index in range(1, len(array)):
        result ^= array[index]
        
    return result
