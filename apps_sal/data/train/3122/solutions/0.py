def chess_triangle(n, m):
    return sum( 8 * (n-x+1)*(m-y+1) for dims in {(3,4), (3,3), (2,4), (2,3)} for x,y in [dims, dims[::-1]] if x <= n and y <= m )

