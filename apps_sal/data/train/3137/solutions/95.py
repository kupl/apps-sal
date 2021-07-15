import math

def round_it(n):

    s = str(n)
    
    v = s.split(".")
    
    if len(v[0])<len(v[1]):
    
        return math.ceil(n)
        
    if len(v[0])>len(v[1]):
    
        return math.floor(n)
        
    else:
    
        return round(n)
        
        
    

