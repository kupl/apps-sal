def xor(a, b):
    return a + b - 2 * a * b


def logical_calc(array, op):
    if op == 'OR':
        result = array[0]
        for value in range(1, len(array)):
            result = result or array[value]
        return result
    if op == 'AND':
        result = array[0]
        for value in range(1, len(array)):
            result = result and array[value]
        return result
    if op == 'XOR':
        result = array[0]
        for value in range(1, len(array)):
            result = xor(result, array[value])
        return result
