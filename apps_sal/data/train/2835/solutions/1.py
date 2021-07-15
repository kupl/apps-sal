def solve(a, b):
  
    PrimList = [2]
    primstr = "2"
    z = 1
    
    while len(primstr) < a+b:
        
        z += 2
        test = 0
        maxsqrt = round(z**0.5)
    
        for p in PrimList:
        
            if p > maxsqrt:
            
                break
        
            if z % p == 0:
            
                test = 1
                break
                
        if test == 1:
        
            continue
                
        PrimList.append(z)
        primstr += str(z)
            
            
    return primstr[a:a+b]
