def logical_calc(array, op):
    state = None
    operation = None

    if op == "AND":
        for i in range(len(array)):
            state = array[i] if i == 0 else state and array[i]
    elif op == "OR":
        for i in range(len(array)):
            state = array[i] if i == 0 else state or array[i]
    elif op == "XOR":
        for i in range(len(array)):
            state = array[i] if i == 0 else state ^ array[i]
    else:
        return f"input - {op} - not recognized"
    
    return state
