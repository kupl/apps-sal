def prime_bef_aft(num):
    after = num + 1
    while not isprime(after):
        after += 1
        
    before = num - 1
    while not isprime(before):
        before -= 1

    return[before, after]
    
    
def isprime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))
