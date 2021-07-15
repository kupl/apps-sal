t = int( input() )
for _ in range(t):
    a, b, n = list(map( int, input().split() ))
    l = [ a, b, a ^ b ]
    print( l[ n % 3 ] )

