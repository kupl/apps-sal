

def logical_calc(array, op):
    print(array)
    print(op)
    print(len(array))
    count_True = 0
    count_False = 0
    for line in array:
        if line == True:
            count_True += 1
        else:
            count_False += 1
    print(count_False)
    print(count_True)
    if op == 'AND':
        if count_True == len(array):
            return True
        else:
            return False
    elif op == 'OR':
        if count_False == len(array):
            return False
        else:
            return True
    elif op == 'XOR':
        if count_True % 2 == 0:
            return False
        else:
            return True
