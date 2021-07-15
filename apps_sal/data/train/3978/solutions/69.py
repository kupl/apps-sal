def check_for_factor(base, factor):
    
    if base < factor:
        return False
        
    if base is factor:
        return True
    else:
        if (base%factor) == 0:
            return True
        else:
            return False
