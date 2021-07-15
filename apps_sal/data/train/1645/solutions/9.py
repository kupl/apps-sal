import math

def is_perfect_sq(n):
    sr = math.sqrt(n)
    low_perfect = math.floor(sr)
    check = sr - low_perfect == 0
    #return check, low_perfect**2
    return check

def sum_of_squares(n):
    """ 
    Based on 
    1. Any number can be represented as the sum of 4 perfect squares
    2. Lagrange's Four Square theorem
    Result is 4 iff n can be written in the form 4^k*(8*m+7)
    """
    # print("Testing value of {}".format(n))
    if is_perfect_sq(n):
        return 1
    
    # Application of Lagrange theorem
    while n % 4 == 0:
        n >>= 2
    if n % 8 == 7:
        return 4
        
    # Check if 2
    for a in range(math.ceil(math.sqrt(n))):
        b = n - a * a
        if is_perfect_sq(b):
            return 2

    return 3

    
    
                   

