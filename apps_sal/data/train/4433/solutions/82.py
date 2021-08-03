def logical_calc(array, op):
    c = len(array)
    res = array[0]
    for i in range(c - 1):
        if op == 'AND':
            res = res and array[i + 1]
        if op == 'OR':
            res = res or array[i + 1]
        if op == 'XOR':
            res = res != array[i + 1]
    return res
