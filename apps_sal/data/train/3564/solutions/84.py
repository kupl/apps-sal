def stringy(size):
    if size == 1:
        return '1'
    elif size % 2 == 0:
        return '10' * (size // 2)
    elif size != 1 and size % 2 == 1:
        return '1' + '01' * (size // 2)
