def power_of_two(x):
    if(x != 0):
        if (x & (x- 1)) == 0:
            return True
        else : 
            return False
    else:
        return False
