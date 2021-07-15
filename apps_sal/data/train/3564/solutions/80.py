def stringy(size):
    r = ""
    for i in range(size):
        if i % 2 == 0:
            r += '1'
        else:
            r += '0'
    return r
