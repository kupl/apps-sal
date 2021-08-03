def stringy(size):
    # Good Luck!
    #t = 0
    for x in range(1, size + 1, 1):
        if x == 1:
            t = '1'
        elif t[-1] == '1':
            t += '0'
        else:
            t += '1'
    return t
