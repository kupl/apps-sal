def stringy(size):
    c = 0
    res = ''
    for i in range(size):
        c += 1
        if i == 0:
            res += '1'
        elif i == 1:
            res += '0'
        elif i % 2 == 0:
            res += '1'
        else:
            res += '0'
    return res
