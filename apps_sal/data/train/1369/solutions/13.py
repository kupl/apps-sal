# cook your dish here
def primes(n):
    count = 0
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            count += p
    return count


cases = int(input())
for i in range(cases):
    l = int(input())
    print(primes(l))
