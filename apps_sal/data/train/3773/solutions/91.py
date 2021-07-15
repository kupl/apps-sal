def isValid(formula):
    d = {1:1, 2:1, 3:2, 4:2, 5:3, 6:3, 7:4, 8:4}
    r = [d[i] for i in formula]
    l = {}
    for x in r:
                
        if (x == 4 and r.count(4) == 1) or (x == 4 and r.count(4) == 2):
            l[4] = True
        if x == 1 and r.count(1) == 1:
            l[1] = True
             
        if x == 2 and r.count(2) == 1:
            l[2] = True
        
        if x == 3 and r.count(3) == 2:
            l[3] = True
        
        
        if  r.count(4) == 0:
            l[4] = False        
        
        if x == 1 and r.count(1) != 1:
            l[1] = False
             
        if x == 2 and r.count(2) != 1:
            l[2] = False
        
        if x == 3 and r.count(3) != 2:
            l[3] = False
        
        
        
        
        
        
        
    result = [k for k in list(l.values())]
    return (sum(result) == len(result))
    
        
    
    
    
    
    

