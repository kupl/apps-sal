import sys
input = sys.stdin.readline
q = int( input() )
rgb = "RGB"
for _ in range( q ):
    n, k = list(map( int, input().split() ))
    s = input()
    ans = n
    for i in range( 3 ):
        r = [ 0 ]
        l = i
        for c in s:
            r.append( r[ -1 ] + ( 1 if c != rgb[ l ] else 0 ) )
            l = ( l + 1 ) % 3
            if len( r ) > k:
                ans = min( ans, r[ -1 ] - r[ len( r ) - 1 - k ] )
    print( ans )

