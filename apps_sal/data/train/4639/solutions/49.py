def power_of_two(x):
    if x == 0:
        return False
    if x == 1:
        return True
    
    while x % 2 == 0:
        x = x // 2
        if x == 1:
            return True
        
    return False
