def sale_hotdogs(n: int) -> int:
    factor = 90
    
    if n < 5 :
        factor = 100
    elif n < 10:
        factor = 95
        
    return n * factor 
