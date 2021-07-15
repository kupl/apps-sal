a, b, c = list(map( int, input().split() ))
n = int( input() )
x = list( map( int, input().split() ) )
print( sum( b < v < c for v in x ) )

