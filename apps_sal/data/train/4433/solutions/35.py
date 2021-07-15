def logical_calc(array, op):
    curr = array[0]
    for x in range(1, len(array)):
        if op == "AND":
            curr = array[x] and curr
        if op == "OR":
            curr = array[x] or curr
        if op == "XOR":
            curr = (array[x] and not curr) or (not array[x] and curr)
    return curr
