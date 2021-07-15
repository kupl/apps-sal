def sum_arrays(array1, array2):
    if len(array1) == 0:
        return array2
    elif len(array2) == 0:
        return array1
    else:
        num1 = int(''.join([str(x) for x in array1]))
        num2 = int(''.join([str(x) for x in array2]))
        result = str(num1 + num2)
        if result == '0':
            return []
        if result[0] == '-':
            lst = ['-' + result[1]]
            lst.extend(result[2:])
            return [int(x) for x in lst]
        else:
            return [int(x) for x in list(result)]

