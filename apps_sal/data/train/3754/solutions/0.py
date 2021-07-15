def isPrime(n):
    return n==2 or n>2 and n&1 and all(n%p for p in range(3,int(n**.5+1),2))

def prime_product(n):
    return next( (x*(n-x) for x in range(n>>1,1,-1) if isPrime(x) and isPrime(n-x)), 0)
