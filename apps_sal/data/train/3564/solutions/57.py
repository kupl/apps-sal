def stringy(size):
    if size % 2 == 0:
        return '10' * int(size // 2)
    else:
        return '10' * int(size // 2) + '1'
