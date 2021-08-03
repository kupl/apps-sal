def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while(p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    c = 0
    for p in range(2, n + 1):
        if prime[p]:
            c += p
    return c % 10


for i in range(int(input())):
    c = SieveOfEratosthenes(int(input()))
    print(c)
