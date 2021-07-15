def my_crib(n):
    
    line    = lambda n,l,m,r: f'{ l }{ m*n }{ r }'.center(W)
    topDoor = lambda: f'|{ ( "_"*half_1 ).center(W-2) }|'
    door    = lambda b: ( b*half_1 ).join('||||')
    
    W, H, half_1 = 6*n+1, 4*n+1, 2*n-1
    
    return '\n'.join( line(2*(n+i)-1, *('/_\\' if i else '___')) if i<=2*n else
                      line(W-2, *'| |')                          if i< 3*n else
                      topDoor()                                  if i==3*n else
                      door('_' if i==4*n else ' ')               for i in range(H) )
