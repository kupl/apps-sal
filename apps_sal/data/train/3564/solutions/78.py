def stringy(size):
    res = ''
    n = 0
    while n < size:
        if n == size:
            break
        else:
            res += '1'
            n += 1
        if n == size:
            break
        else:
            res += '0'
            n += 1
    return res
