def pattern(n):
    return '\n'.join( ''.join(str(j) for j in range(i,n+1)) for i in range(1,n+1) )
