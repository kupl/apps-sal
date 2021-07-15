def is_triangle(a, b, c):
    # Check if sum of 2 sides is bigger than the last size
    if a + b > c and a + c > b and b + c > a:
        return True
    
    return False

