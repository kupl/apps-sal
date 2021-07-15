evenDigits = ['0', '2', '4', '6', '8']

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def evenDigitCount(n):
    count = 0
    for c in str(n):
        if c in evenDigits:
            count += 1
    return count

def f(n):
    allPrimes = primes(n)
    p = allPrimes[0]
    mostEvenDigits = evenDigitCount(p)
    for prime in allPrimes:
        thisPrimesEvenDigits = evenDigitCount(prime)
        if thisPrimesEvenDigits >= mostEvenDigits:
            p = prime
            mostEvenDigits = thisPrimesEvenDigits
    
    return p

