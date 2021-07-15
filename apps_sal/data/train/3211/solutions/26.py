def divide(weight):
    
    check_even = weight - 2
    
    if check_even <= 0:
        return False
    
    if check_even % 2 == 0:
        return True
    else:
        return False
