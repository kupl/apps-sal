def stringy(size):
    res = ''
    for x in range(0, size):
        res += '1' if x % 2 == 0 else '0'
    return res
