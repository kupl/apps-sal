def logical_calc(array, op):
    bool = array[0] == True
    for i in range(1, len(array)):
        if op == "AND":
            bool = bool & array[i]
        elif op == "OR":
            bool = bool | array[i]
        elif op == "XOR":
            bool = bool ^ array[i]
    return bool == True
