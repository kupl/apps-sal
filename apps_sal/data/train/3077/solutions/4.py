def pattern(n):
    return '\n'.join( [ ''.join(map(str, range(i,n+1))) for i in range(1, n+1) ] )
