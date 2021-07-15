def collatz(n):
    ret = []
    while n!= 1:
        ret.append(n)
        n = [n//2, (n*3)+1][n%2]    
    return '->'.join( map( str, ret+[1] ) )
