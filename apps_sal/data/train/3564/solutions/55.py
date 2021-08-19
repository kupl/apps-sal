def stringy(size):
    print(size)
    bla = ''
    for i in range(int(size)):
        if i % 2 != 0:
            bla += str(0)
        else:
            bla += str(1)
    print(bla)
    return bla


size = 3
stringy(size)
