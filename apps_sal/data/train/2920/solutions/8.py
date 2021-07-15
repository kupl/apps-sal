def pattern(n):
    return '\n'.join([''.join(map(str,list(range(n,n-i,-1)))) for i in range(1,n+1)])
