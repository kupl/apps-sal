def stringy(size):
    res = ''
    t = size
    while t > 0:
        if t % 2 == 1:
            res = '1' + res
        else:
            res = '0' + res
        t -= 1
    return res
