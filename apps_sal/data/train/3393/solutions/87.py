from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def list_squared(m, n):
    result = []
    
    for i in range(m, n+1):
        factors_sq = [x**2 for x in factors(i)]
        sum_factors = sum(factors_sq)
        sum_factors_root = sum_factors ** 0.5
        if  sum_factors_root == int(sum_factors_root):
            result.append([i, sum_factors])
            
    return result
        

