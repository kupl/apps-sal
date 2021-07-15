import math
def gap(g, m, n):
    prev = None
    curr = None
    for i in range(m, n + 1):
        if isPrime(i):
            if prev and i - prev == g:
                curr = i
                break
            prev = i  
    if curr:         
        return [prev, curr]
    else:
        return None
    
def isPrime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

