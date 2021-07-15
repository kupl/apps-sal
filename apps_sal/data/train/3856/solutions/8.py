def solve(a,b):

    
    range_n = b+1 
    is_prime = [True] * range_n
    primes = [0]
    result = 0
    for i in range (2, range_n):
        if is_prime[i]:
            primes += i,
            for j in range (2*i, range_n, i):
                is_prime[j] = False

    for i in range (2, len(primes)):
        if primes[i] >= a and is_prime[i]: result += primes[i]
            
    return result
