def find_difference(a, b):
    
    m = 1
    n = 1
    
    for x in range(len(a)) :
        m *= a[x]
        n *= b[x]
        
    return abs(m - n)    
