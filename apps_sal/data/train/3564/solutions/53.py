def stringy(size):
    s = ''
    for i in range(0,size):
        if i % 2:
            s += '0'
        else:
            s += '1'
    return s
