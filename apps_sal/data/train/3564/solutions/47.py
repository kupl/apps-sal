def stringy(size):
    num = '10'
    if size % 2 == 0:
        return num * (size // 2)
    else:
        return (((size - 1) // 2) * num) + '1'
