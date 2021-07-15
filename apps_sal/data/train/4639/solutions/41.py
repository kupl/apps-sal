def power_of_two(x):
  # your code here
    if x == 0:
        return False
    
    while( x != 1):
        print(x)
        if (x % 2) != 0:
            return False
        else:
            x /= 2
            
    
    return True
