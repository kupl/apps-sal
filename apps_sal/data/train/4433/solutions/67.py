def logical_calc(array, op):
    bool = array[0]
    if op == 'AND':
        for n in range(len(array) - 1):
            bool = bool and array[n + 1]
    elif op == 'OR':
        for n in range(len(array) - 1):
            bool = bool or array[n + 1]
    elif op == 'XOR':
        for n in range(len(array) - 1):
            bool = (bool or array[n + 1]) and (not (bool and array[n + 1]))
    else:
        bool = False
    return bool
