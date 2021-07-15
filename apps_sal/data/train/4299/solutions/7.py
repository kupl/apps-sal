def isPrime(n): 
    for i in range(2,int(n**.5)+1): 
        if n%i == 0:
            return False
    return True 
def is_prime_happy(n):
    sum = 0
    for i in range(2,n): 
        if isPrime(i): 
            sum += i 
    if sum > 0 and not sum%n: 
        return True
    return False 
