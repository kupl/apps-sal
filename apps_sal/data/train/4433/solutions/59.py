def logical_calc(array, op):
    val = array.pop()
    for i in array:
        if op == 'AND':
            if not i:
                return False
        elif op == 'OR':
            if i:
                return True
        else:
            val ^= i;
    return val
