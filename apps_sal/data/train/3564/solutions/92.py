def stringy(size):
    s = '10' * (size // 2)
    s = s + '1'
    return '10' * (size // 2) if size % 2 == 0 else s
