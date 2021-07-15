def is_triangle(a, b, c):
    max_int = max(a,b,c)
    min_int = min(a,b,c)
    
    
    if max_int == a:
        sum = b + c
        if sum > a:
            return True
    if max_int == b:
        sum = a + c
        if sum > b:
            return True
    if max_int == c:
        sum = a + b
        if sum > c:
            return True
            
    return False

