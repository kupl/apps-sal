def logical_calc(array, op):
    res = array[0]
    if op == 'AND':
        for i in range(1, len(array)):
            res *= array[i]
    elif op == 'OR':
        for i in range(1, len(array)):
            res |= array[i]
    else:
        for i in range(1, len(array)):
            res ^= array[i]
    return res
