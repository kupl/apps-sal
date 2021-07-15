def check(a, x): 
    
    try:
    
        bool(a.index(x))
        
        return True
      
    except:
    
        return False
