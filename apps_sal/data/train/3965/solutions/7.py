def powerof4(n):
    
    if not str(n).isdigit(): return False
    else: n = int(n)
    
    while n > 4:
        n = n / 4
    
    if n == 4 or n == 1: return True
    
    return False
