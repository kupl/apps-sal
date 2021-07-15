def logical_calc(array, op):
    first = array[0]
    for i in range(0, len(array)-1):
        if op == "AND":
            first = array[i+1] and first
        elif op == "OR":
            first = array[i+1] or first
        elif op == "XOR":
            first = array[i+1] ^ first
    return first
