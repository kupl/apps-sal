def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
def gap(g, m, n):
    for i in range(m,n+1):
        if isPrime(i) and isPrime(i+g) and not any(isPrime(i+j) for j in range(1,g)):
            return [i,i+g]
            

