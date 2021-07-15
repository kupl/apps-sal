def stringy(size):
    l = ''
    for x in range(size):
        if x % 2 == 0:
            l += '1'
        else:
            l += '0'
    return l
