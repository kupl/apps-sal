def divisors(n):
    
    count = 0
    for i in range(1, int(n / 2) + 1):
        
        if n % i == 0:
            count += 1
    
    count += 1 #n value itself
            
    return count
