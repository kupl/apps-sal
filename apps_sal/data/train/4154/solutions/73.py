def is_triangle(a, b, c):
    if a >= b+c or b >= c+a or c >= b+a:
        return False;
    else:
        return True
    

