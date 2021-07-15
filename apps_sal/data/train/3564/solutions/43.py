def stringy(size):
    result = ''
    for el in range(size):
        if el % 2 == 0:
            result += '1'
        else:
            result += '0'
    return result
