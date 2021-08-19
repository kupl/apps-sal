def stringy(size):
    res = ''
    for i in range(0, size):
        if i % 2 == 0:
            res = res + '1'
        else:
            res = res + '0'
    return res
