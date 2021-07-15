def sum_triangular_numbers(n):
    
    if n<0:
        
        return 0
    
    a = list(range(1,n+1))
    
    b = []
    
    for i in range(0,len(a)):
        
        d = a[i]+sum(a[0:i])
        
        b.append(d)
    
    s = sum(b)
    
    return s


