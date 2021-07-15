def has_two_cube_sums(n):
    if n == 1: return False
    
    high = int((n)**(1/3.0))
    low  = int((n/2)**(1/3.0))
    return sum( abs(y-round(y)) < 1e-8 for y in [((n-x**3))**(1/3.0) for x in range(low,high+1)]) >= 2
