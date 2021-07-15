import math

def get_divisors(num):
    divisors = {1}
    
    if num == 1:
        return divisors
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num/i)
    divisors.add(num)
    
    return list(divisors)

def list_squared(m, n):
    res = []
    
    for i in range(m,n+1):
        total = sum([x*x for x in get_divisors(i)])
        if int(math.sqrt(total))**2 == total:
            res.append([i,total])
    
    return res

