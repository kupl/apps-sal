def stringy(size):
    if size == 0:
        return ''
    result = '1'
    for i in range(1, size):
        if((i % 2) != 0):
            result += '0'
        else:
            result += '1'
    return result
