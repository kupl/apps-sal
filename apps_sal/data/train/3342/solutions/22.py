def pattern(n):
    return ''.join([str(x)*x+'\n' for x in range(1,n+1)])[:-1]
