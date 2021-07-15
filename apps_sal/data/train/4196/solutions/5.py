import math
def summationOfPrimes(primes):
    s = 0
    j = 0
    while j<=primes:
        if isprime(j):
            s+=j
        j+=1
    return s-1
  
  
def isprime(n):
    if n <=3:
        return True
    i = 2
    while i <= math.sqrt(n):    
        if n%i == 0:
            return False
        i += 1
    return True
