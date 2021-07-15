def pattern(n):
    strx = ''
    for x in range(1, n+1):
        strx += str(x)*x + '\n'
    return strx[:-1]
