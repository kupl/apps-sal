def findSquares(x,y):
    squares = 0
    while y > 0:  
        squares = squares + x*y
        x = x-1
        y = y-1
    return squares

