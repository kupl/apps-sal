def stringy(size):
    if size % 2 == 0:
        n = size // 2
        return '10' * n
    else:
        n = (size + 1) // 2 - 1
        return '10' * n + '1'
