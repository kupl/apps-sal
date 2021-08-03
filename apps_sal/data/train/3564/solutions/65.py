def stringy(size):
    x = []
    for i in range(size):
        if i % 2 == 0:
            x.append('1')
        else:
            x.append('0')
    return ''.join(x)
