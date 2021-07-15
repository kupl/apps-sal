def pattern(n):
    s = ''
    for i in range(n):
        s += str(n)
        for ni in range(n-1,i,-1):
            s += str(ni)
        if n-1 == i:
            pass
        else:
            s += '\n'
    return s
