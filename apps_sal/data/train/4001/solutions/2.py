def dot(n,m):
    sep = '---'.join( '+'*(n+1) )
    dot = ' o '.join( '|'*(n+1) )

    return f'\n{dot}\n'.join( [sep for _ in range(m+1) ])  
