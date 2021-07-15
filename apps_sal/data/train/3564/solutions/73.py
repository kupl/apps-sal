def stringy(size):
    res = ''
    for i in range(size):
        if i % 2 == 1:
            res += '0'
        else:
            res += '1'
    return res
