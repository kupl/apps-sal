def logical_calc(array, op):
    start = array[0]
    for i in range(1, len(array)):
        if op == "AND":
            start = start and array[i]
        elif op == "OR":
            start = start or array[i]
        elif op == "XOR":
            if start == array[i]:
                start = False
            else:
                start = True
    return start
