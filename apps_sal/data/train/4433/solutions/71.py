def logical_calc(array, op):
    a = array[0]
    if op == 'AND':
        for i in range(len(array)-1):
            a = a and array[i+1]
        return bool(a)
    elif op == 'OR':
        for i in range(len(array)-1):
            a = a or array[i+1]
        return bool(a)
    elif op == 'XOR':
        for i in range(len(array)-1):
             a = a != array[i+1]
        return bool(a)

