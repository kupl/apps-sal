def logical_calc(array, op):
    if op == 'AND':
        for item in array:
            if item is False:
                return False
        return True

    elif op == 'OR':
        for item in array:
            if item is True:
                return True
        return False

    else:
        a = len([a for a in array if a is True])
        if a % 2 != 0 and a > 0:
            return True
        return False
