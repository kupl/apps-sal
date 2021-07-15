def logical_calc(array, op):
    bool = array[0]
    for x in range(1, len(array)):
        if op == 'AND':
            bool = array[x] & bool
        if op == 'OR':
            bool = array[x] | bool
        if op == 'XOR':
            bool = array[x] ^ bool
    return bool
