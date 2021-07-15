from math import floor, sqrt

def points(n):
    # solution is 
    # A000328       Number of points of norm <= n^2 in square lattice.
    # which can be calculated as 
    # a(n) = 4*A000603(n) - (4*n+3), n >= 0 where
    # A000603       Number of nonnegative solutions to x^2 + y^2 <= n^2
    # which can be calculated as 
    # a(n) = A001182(n) + 2*n + 1 where
    # A001182       Number of cells of square lattice of edge 1/n inside quadrant of unit circle centered at 0
    A001182 = sum(floor(sqrt(n**2-k**2)) for k in range(1,n))
    A000603 = A001182 + 2*n + 1
    A000328 = 4*A000603 - (4*n+3) 
    return A000328

