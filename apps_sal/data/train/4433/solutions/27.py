def logical_calc(array, op):
    # convert bool array values to str and join them with the specified operator
    # return the results using eval() on the resulting string
    return eval({'AND': '&', 'OR': '|', 'XOR': '^'}[op].join(map(str, array)))
