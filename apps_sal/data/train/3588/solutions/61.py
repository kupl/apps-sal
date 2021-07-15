def quadratic(x1, x2):
    a = 1 
    if x1 < 0:
        c = x1 * x2 
    
    else:
        c = x1 * x2
        
    if x1 > 0 or x2 > 0:
        b = -(x1 + x2) 
    else:
        b = abs(x1 + x2) 
    tuple = (a, b , c)
    return tuple
