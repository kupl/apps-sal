def stringy(size):
    S = ''
    nextChar = '1'
    for i in range(size):
        S += nextChar
        if nextChar == '1':
            nextChar = '0'
        else:
            nextChar = '1'
    return S
