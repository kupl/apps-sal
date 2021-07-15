def pyramid(n):
    
    A = list()
    
    for i in range(1, n + 1):
    
        a = list()
        
        for j in range(i): a.append(1)
        
        A.append(a)
        
    return A
