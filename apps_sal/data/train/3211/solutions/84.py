def divide(x):
    if x % 2 == 0 and x/2%2 == 0:
        return True
    
    if x % 2 == 0 and x/2%2 != 0:
        
        if (x/2-1)%2 == 0 and (x/2+1)%2 == 0 and (x/2-1) != 0:
            return True
        else:
            return False
    
    return False
