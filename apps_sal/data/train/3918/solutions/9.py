def baby_count(x):
    
    s = x.lower()
    
    a = s.count("a")
    
    b = s.count("b")
    
    d = b//2
    
    y = s.count("y")
    
    z = [a,d,y]
    
    m = min(z)
    
    if m==0:
        
        return "Where's the baby?!"
    
    else:
    
        return m

