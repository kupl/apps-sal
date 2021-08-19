def fac(a):
    s = 1
    for i in range(1, a + 1):
        s = s * i
    return s


def prime(n):
    n = int(n)
    if(n == 2 or n == 3):
        return 1
    k = n**(1 / 2)
    for i in range(2, int(k) + 2):
        if(n % i == 0):
            return 0
    return 1


def sieve(n):
    arr = []
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            arr.append(p)
    return arr


t = int(input())
# n,m=[int(x) for x in input().split()]

for ii in range(t):
    n, m = [int(x) for x in input().split()]
    if(n == 1):
        print(m)
    else:
        if(m % 2 == 0):
            m -= 1
        print(m // 2)
