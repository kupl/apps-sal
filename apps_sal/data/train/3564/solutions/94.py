def stringy(size):
    res = ''
    n = True
    for i in range(size):
        if n:
            res += '1'
            n = False
        else:
            res += '0'
            n = True
    return res
