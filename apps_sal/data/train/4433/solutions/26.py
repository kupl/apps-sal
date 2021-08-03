def logical_calc(array, op):
    # dictionary

    return eval({'AND': '&', 'OR': '|'}.get(op, '^').join(str(i) for i in array))

    # string
    # return eval((op.lower() if op!='XOR' else '^').join(' '+str(i)+' ' for i in array))
