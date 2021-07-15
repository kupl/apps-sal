def logical_calc(array, op):
    log = array[0]
    for i in array[1:51]:
        if op == "AND":
            log = log and i
        elif op == "OR":
            log = log or i
        else:
            log = log ^ i
    return log

