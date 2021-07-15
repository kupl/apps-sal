def starts_with(st, prefix): 
    x = len(prefix)
    if len(prefix) > len(st):
        return False
    if st[:x] == prefix:
        return True
    return False
    
        
        
    

