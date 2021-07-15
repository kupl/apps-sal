def logical_calc(array, op):
    if op == 'XOR':
        result = array[0]
        for element in array[1:]:
            if element == result:
                result = False
            else:
                result = True
        return result
    return all(array) if op =='AND' else any(array)
