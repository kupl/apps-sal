def logical_calc(array, op):
    ans = array[0]
    for i in array[1:]:
        if op == 'AND':
            ans = ans & i
        elif op == 'OR':
            ans = ans | i
        else:
            ans = ans ^ i
    return ans
