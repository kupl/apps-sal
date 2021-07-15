# Miller-Rabin primality test 

from random import randrange

def prime_or_composite(n):
    if n < 10: 
        return 'Probable Prime' if n in [2, 3, 5, 7] else 'Composite'
        
    def miller_test(a, d): 
        p = pow(a, d, n)
        if p == 1 or p == n - 1: 
            return False
        
        while d != n - 1 and p != 1 and p != n - 1: 
            p = p ** 2 % n
            d *= 2
            
        return False if p == n - 1 else True
    
    d = n - 1
    
    while d % 2 == 0: 
        d >>= 1
    
    for i in range(8): 
        a = randrange(2, n - 1)
        if miller_test(a, d): 
            return 'Composite'
        
    return 'Probable Prime'
