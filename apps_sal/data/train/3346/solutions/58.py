def gap(g,m,n):
    prev = float('inf')
    for i in range(m, n+1):
        prime = True
        for j in range(2, int(i**.5) + 1):
            if i%j==0:
                prime = False
                break 
        if prime == True and (i - prev == g):
            return [prev, i]
        prev = i if prime else prev #previous prime number
    return None
    
    
    
    

