def stringy(size):
    x = ''
    while len(x) < size:
        x += '1'
        if len(x) < size:
            x += '0'
    return x
