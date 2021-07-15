def is_triangle(a, b, c):
    if a + b > c:
        
        if a + c > b:
        
            if b +c > a:
                return True
            else:
                return False
        
        else:
            return False
        
    else:
        return False

    
    return False

