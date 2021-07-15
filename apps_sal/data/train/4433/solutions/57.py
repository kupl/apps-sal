def logical_calc(array, op):
    if op == 'AND':
        for bool in array:
            if bool == False:
                return False
        return True
    elif op == 'OR':
        for bool in array:
            if bool == True:
                return True
        return False
    else:
        aux = array[0]
        i = 1
        while i < len(array):
            if aux != array[i]:
                aux = True
            else:
                aux = False
            i+=1
        return aux
