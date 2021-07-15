def halving_sum(n):
    
    x = 2
    sol = n
    
    while (n//x)>0:
        sol = sol + n//x
        x*=2
        
    return sol
