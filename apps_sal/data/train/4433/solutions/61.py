def logical_calc(array, op):
    if op == 'XOR':
        op = '^'
    op = op.lower()
    array = [str(i) for i in array]
    arr2 = []
    for i in range(len(array)):
        arr2.append(array[i])
        arr2.append(op)
    arr2 = arr2[0:-1]

    return eval(' '.join(arr2))
