def stringy(size):
    s = ''
    for i in range(0, size):
        if(i % 2 == 0):
            j = "1"
            s = s + j
        else:
            j = "0"
            s = s + j
    return s
