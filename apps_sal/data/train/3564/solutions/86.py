def stringy(size):
    s = ''
    for i in range(1, size + 1):
        if i % 2 == 0:
            s += str(0)
        else:
            s += str(1)
    return s
