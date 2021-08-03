def stringy(size):
    if size == 1:
        return '1'
    if size % 2 == 0:
        return '10' * int(size / 2)
    return '10' * int((size - 1) / 2) + '1'
