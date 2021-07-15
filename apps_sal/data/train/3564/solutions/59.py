def stringy(size):
    result = '10' * (size // 2)
    if size % 2 == 1:
        result = result + '1'
    return result
