def stringy(size):
    x = ''
    n = 1
    while n <= size:
        if n % 2 == 1:
            x += '1'
            n += 1
        else:
            x += '0'
            n += 1
    return x
