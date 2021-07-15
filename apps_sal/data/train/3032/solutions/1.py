def factorsRange(n, m):
    res = {}
    
    for num in range(n, m+1):
        factors = []
        
        for div in range(2, num // 2 + 1):
            if num % div == 0:
                factors.append(div)
        
        if len(factors) == 0:
            factors = ['None']
        
        res[num] = factors
    
    return res
