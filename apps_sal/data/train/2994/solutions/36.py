def find_digit(num, nth):
    
    if nth<=0:
        
        return -1
    
    n = abs(num)
    
    d = [int(x) for x in str(n)]
    
    l = len(d)
    
    if nth>l:
        
        return 0
    
    else:
    
        p = d[::-1]
    
        for i,j in enumerate(p,1):
        
            if i==nth:
            
                return j

