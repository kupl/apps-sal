def x(n):    
    d = [[0] * n for i in range (n)]
    for i in range(n):
        d[i][i] = 1
        d[i][-i-1] = 1
    return d
