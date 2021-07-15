def is_prime(n):
    'Return True if n is a prime number otherwise return False'
    # 0 and 1 are not primes
    if n < 2: 
        return False
    
    # 2 is only even prime so reject all others
    if n == 2: 
        return True
        
    if not n & 1: 
        return False
    
    # test other possiblities
    for i in range(3, n):
        if (n % i) == 0 and n != i: 
            return False
  
  
    return True
