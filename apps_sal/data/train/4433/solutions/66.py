def logical_calc(array, op):
    if op == 'AND':
        return False not in array
    elif op == 'OR':
        return True in array
    elif op == 'XOR':
        s1 = sum(array)
        if s1 % 2 == 0:
            return False
        else:
            return True
