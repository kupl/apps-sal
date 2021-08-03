# cook your dish here
def primes(n):
    prime = [True] * (n + 1)
    p = 2
    while(p * p <= n):
        if(prime[p] == True):
            i = p * 2
            while(i <= n):
                prime[i] = False
                i += p
        p += 1
    sum = 0
    for i in range(2, n + 1):
        if(prime[i]):
            sum += i
    return sum


t = int(input())
for i in range(t):
    n = int(input())
    print(primes(n))
