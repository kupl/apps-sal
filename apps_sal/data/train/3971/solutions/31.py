def tidyNumber(n):
    n = str(n)
    p = 0
    for i in n:
        if int(i) < int(p):
            return False
        else:
            p = i
    
    return True
        
            
        

