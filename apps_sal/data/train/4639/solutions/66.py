def power_of_two(x):
    
    if x <= 0:
        return False
    if x == 1:
        return True
        
    test = 1
    i = 0
    
    while test <= x:
        test = test * 2
        if test == x:
            return True
    
    return False
